def miniskil_chenn(input_str):
        return list(input_str.lower().split())

def majiskil_premye_let(input_str):
        words = input_str.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)

def nouvo_chenn_ak_inisyal(input_str):
        inisyal = [word[0] for word in input_str.split()]
        return "".join(inisyal)


def ranplase_a_avek_at(input_str):
        replaced_str = input_str.replace('a', '@')
        return replaced_str[:1].lower() + replaced_str[1:].upper()


def endeks_premye_a(input_str):
        return input_str.find('a')

def total_endeks_a(input_str):
        return sum([i for i, char in             enumerate(input_str) if char.lower() == 'a'])


def lis_endeks_miniskil_a(input_str):
        return [i for i, char in enumerate(input_str)          if char.islower() and char == 'a']


def retire_espas_kole_kantite(input_str):
        no_spaces_str = input_str.replace(' ', '')
        return no_spaces_str, len(no_spaces_str)

