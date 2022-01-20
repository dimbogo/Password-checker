import requests
import hashlib
import sys

def request_api_data(query_char): # requesting the API, result is the list of all matches with our password's chunk at the beginning
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    return res

def get_passwords_leaks_count(hashes, hash_to_check): # dividing the bulk of data into tuples with a hash of every password and a counter of how many times this password has been hacked
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check: #checking whether our password is in the list
            return count
    return 0

def pwned_api_check(password): #taking a password as an argument and encoding it by SHA1 algorithm
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:] # slicing the encoded password to prevent leaking of password, so we will import only 5 first characters of our password to a third party API and work with the results (a few hundred of passwords)
    response = request_api_data(first5_char)
    return get_passwords_leaks_count(response, tail)

def main(inputs): #main function that triggers other function to actually check for passwords being hacked
    for password in inputs:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f"{password} was NOT found. Carry on!")
    return "done!"

inputs = []

if __name__ == '__main__':
    with open(sys.argv[1]) as file: # unpacking txt file with passwords, adding them to the list
        for line in file:
            for element in line.strip().split():
                inputs.append(element)

    sys.exit(main(inputs))