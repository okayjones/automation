import re

PHONE_REGEX = r'\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})'
EMAIL_REGEX = r'([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5})'

def scrape_phone_numbers(content: str) -> str:
    unique_matches = list(set(re.findall(PHONE_REGEX, content)))
    number_list = ['-'.join(p) for p in unique_matches]
    number_list.sort()
    phone_numbers = '\n'.join(number_list)
    return phone_numbers

def scrape_email(content: str)-> str:
    unique_matches = list(set(re.findall(EMAIL_REGEX, content)))
    unique_matches.sort()
    emails = '\n'.join(unique_matches)
    return emails

def write_file(path:str, content):
    with open(path, 'w+') as f:
        f.write(content)

if __name__ == '__main__':
    with open('./assets/potential-contacts.txt', 'r') as f:
        contents = f.read()

    write_file('./assets/phone_numbers.txt', scrape_phone_numbers(contents))
    write_file('./assets/emails.txt', scrape_email(contents))