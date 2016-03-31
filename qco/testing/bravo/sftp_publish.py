import pysftp

hostname = ''
username = ''
password = ''


def put_file(location):
    with pysftp.Connection(hostname, username, password) as sftp:
        with sftp.cd('public'):  # temporarily chdir to public
            sftp.put(location)  # upload file to public/ on remote


