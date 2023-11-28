import re

import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

from sentence_splitter import SentenceSplitter, split_text_into_sentences

splitter = SentenceSplitter(language='en')

from evaluate import load

google_bleu = load("google_bleu")


async def paraphrase_text(full_text, num_return_sequences=10):
    every = []
    sentence_list = splitter.split(full_text)
    for input_text in sentence_list:
        batch = tokenizer.prepare_seq2seq_batch([input_text], truncation=True, padding='longest', max_length=60,
                                                return_tensors="pt").to(torch_device)
        translated = model.generate(**batch, max_length=60, num_beams=10, num_return_sequences=num_return_sequences,
                                    temperature=1.5)
        every.append(tokenizer.batch_decode(translated, skip_special_tokens=True))
    worst = 1
    worst_sen = ''
    paraphrased_text = ''
    for i in range(len(every)):
        for k in range(len(every[i])):
            results = google_bleu.compute(predictions=[sentence_list[i]], references=[every[i][k]])
            if results["google_bleu"] < worst:
                worst = results["google_bleu"]
                worst_sen = every[i][k]
        paraphrased_text += worst_sen + ' '
        worst = 1
        worst_sen = ''

    return paraphrased_text
