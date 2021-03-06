import gpg_wrapper

input_data = {
    'key_type': 'RSA',
    'key_length': 1024,
    'key_usage': 'ESCA',
    'subkey_type': 'RSA',
    'subkey_length': 1024,
    'subkey_usage': 'encrypt,sign,auth',
    'name_email': 'test_sami@mydomain.com',
    'passphrase': 'Operation'
}
input_data1 = {
    'key_type': 'RSA',
    'key_length': 1024,
    'key_usage': 'ESCA',
    'subkey_type': 'RSA',
    'subkey_length': 1024,
    'subkey_usage': 'encrypt,sign,auth',
    'name_email': 'test@mydomain.com',
    'passphrase': 'Security'
}
key_pair = gpg_wrapper.gpg_key('gpghome1')
# key_pair.delete_key('test@mydomain.com')
# key_pair.generate_key(input_data)
# key_pair.list_public_keys()
# public_key = key_pair.export_public_key('test_sami@mydomain.com')

gpg = gpg_wrapper.gpg_key('gpghome')
# gpg.delete_key('test@mydomain.com')
# gpg.import_public_key(public_key)
# gpg.generate_key(input_data1)
# gpg.list_public_keys()


gpg = gpg_wrapper.gpg_object('gpghome', 'test@mydomain.com', 'Security')
fingerprint, hash, passphrase = \
    gpg_wrapper.blockchain_encrypt(
        b'I wish you a Merry Christmas',
        'gpghome',
        'test@mydomain.com',
        'Security'
    )
de_passphrase = gpg.decrypt_assym_message(passphrase)
print(de_passphrase)
de_hash = gpg.decrypt_sym_message(hash, de_passphrase.decode())
print(de_hash)

signature = gpg.sign_message(b'Decorate a Christmas tree')
print(gpg.verify_signature(b'Decorate a Christmas tree', signature))
