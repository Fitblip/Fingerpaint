import platform
import re
import os
from subprocess import Popen, PIPE

DEVNULL = open(os.devnull,'r')

# Get the right openssl binary
if platform.system() == "Windows":
  # If on windows, use the cygwin openssl
  openssl_binary = 'C:\\cygwin\\bin\\openssl'
else:
  # Just look in the default search path
  openssl_binary = "openssl"

# An implementation of the SDBM hashing algorithm.
def sdbm(string):
  hash = 0
  for chr in string:
    char = ord(chr)
    hash = char + (hash << 6) + (hash << 16) - hash
  return hash

# Convert the hash that comes back to an html RGB color
def hashToColor(string):
  hash = sdbm(string)
  r = (hash & 0xFF0000) >> 16
  g = (hash & 0x00FF00) >> 8
  b = hash & 0x0000FF
  return "#%02x%02x%02x" % (r, g, b)

def matchDomainToColor(hostname):
  if ":" not in hostname:
    hostname = hostname + ":443"
  # If someone puts something fishy in, bail out
  if not re.match(r'^[a-zA-Z\.\:0-9]*$',hostname):
    raise Exception("Bad characters!")
  p = Popen([
              openssl_binary,
              's_client',
              '-showcerts',
              '-connect',
              hostname
            ], stdout=PIPE, stderr=PIPE, stdin=DEVNULL)

  OpenSSLOutput = p.stdout.read()

  certs = re.findall(
    r'^(\-{5}BEGIN\sCERTIFICATE\-{5}.*?\-{5}END\sCERTIFICATE\-{5})',
    OpenSSLOutput,
    re.MULTILINE | re.DOTALL
  )
  if not certs:
    raise Warning("Hostname has no certs!")

  certChain = []
  for cert in certs:
    certInfo = Popen([
                openssl_binary,
                'x509',
                '-fingerprint',
                '-noout'
                ],
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE
    )
    certFingerprint = certInfo.communicate(input=cert)[0]
    certFingerprint = certFingerprint.split("=")[-1]
    certFingerprint = certFingerprint.strip()
    certFingerprint = certFingerprint.replace(':','')
    certChain.append(str(certFingerprint))

  allFingerprints = "".join(certChain)
  return hashToColor(allFingerprints)
