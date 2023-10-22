import re


async def str_to_list(text):
    res = [x for x in re.split("[//.|//!|//?]", text) if x != ""]
    return res