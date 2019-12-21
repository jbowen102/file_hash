import hashlib


def file_hash(full_path, hash_type):
    """
    Returns hash of file identified by full_path.
    Possible hash_types: 'md5', 'sha1', 'sha256' (passed as string)
    """
    with open(full_path, 'rb') as file_obj:

        if hash_type == 'md5':
            file_hash = hashlib.md5(file_obj.read())
        elif hash_type == 'sha1':
            file_hash = hashlib.sha1(file_obj.read())
        elif hash_type == 'sha256':
            file_hash = hashlib.sha256(file_obj.read())
        else:
            raise ValueError("Valid hash_types: 'md5', 'sha1', 'sha256'")

        return file_hash.hexdigest()
