Fingerpaint
===========

Fingerpaint is a library/method for mapping chains of fingerprints (e.g. SSL) to a color. This is inspired by Chrome's UI redesign to help hedge against phishing attacks. This will be able to have some better indication that a servers fingerprint has changed in some way. 

*Note* This is /really/ rough. I don't like calling out to openssl directly, but python's ssl only supports getting the full chain in python3, and compiling M2Crypto to parse the cert is a total pain.