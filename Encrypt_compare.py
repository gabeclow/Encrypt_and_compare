import hashlib

open('sha256list', 'w').close()
open('email_matches', 'w').close()


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def write_result(email):
    doc = open('email_matches', "a")
    doc.write(email)
    doc.close()


def add_sha_email(email):
    doc = open('sha256list', "a")
    doc.write(encrypt_string(email))
    doc.write("\n")
    doc.close()


def add_match(email):
    doc = open('email_matches', "a")
    doc.write(email)
    doc.write("\n")
    doc.close()


# open the client_provided_email list
client_provided_email_list = open('metadata_emails', "r")

# convert to sha256 list
for line in client_provided_email_list:
    add_sha_email(line)


# compare the sha256 list to client_provided_sha_list

list1 = open('sha256list')

dictionary = dict((k, i) for i, k in enumerate(list1))

list2 = open('client_encrypted_emails')

intersection = set(dictionary).intersection(list2)
# get position of comparison
indices = [dictionary[x] for x in intersection]
# print(indices)


with open('metadata_emails') as f:
    lines = f.read().splitlines()

for entry in indices:
    # add item from position in client_provided_email list to email_matches file
    print(lines[entry])
    add_match(lines[entry])








