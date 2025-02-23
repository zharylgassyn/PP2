import re

print(bool(re.fullmatch(r"ab*", "abbb")))  # 1

print(bool(re.fullmatch(r"ab{2,3}", "abb")))  # 2

print(re.findall(r"\b[a-z]+_[a-z]+\b", "abc_def xyz_uvw a_b_c"))  # 3

print(re.findall(r"[A-Z][a-z]+", "Hello World Test"))  # 4

print(bool(re.fullmatch(r"a.*b", "axxxb")))  # 5

print(re.sub(r"[ ,.]", ":", "Hello, world. This is Python"))  # 6


def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s).capitalize()

print(snake_to_camel("hello_world_python"))  # 7


print(re.split(r"(?=[A-Z])", "HelloWorldPython"))  # 8

print(re.sub(r"([a-z])([A-Z])", r"\1 \2", "HelloWorldPython"))  # 9

print(re.sub(r"([a-z])([A-Z])", r"\1_\2", "HelloWorldPython").lower())  # 10