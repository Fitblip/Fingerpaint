Fingerpaint
===========

Fingerpaint is a library/method for mapping chains of fingerprints (e.g. SSL) to a color. This is inspired by Chrome's UI redesign to help hedge against phishing attacks. This will be able to have some better indication that a servers fingerprint has changed in some way. 

*Note* This is /really/ rough. It does some silly crap and I know it. It was a weekend project (not even). I don't like calling out to openssl directly, but python's ssl only supports getting the full chain in python3, and compiling M2Crypto to parse the cert is a total pain. If I have precious time to code I'll absolutely incur technical debt to get an idea working. Pull requests are ALWAYS welcome. 

How does it work?
=================

It's pretty stupidly simple, actually. Each chain's fingerprints are concatinated together in order the chain is presented (root cert last). That is passed through the sdbm hashing algorithm then some bit-shifts to finally reach an HTML color. Of course as I'm typing this I realize I can just lop off the end of an MD5(), so that'll happen soon. Damn it. 

Dude, why?
==========

Mostly just to code something this weekend, but this chrome UX security thing got me thinking, and while current browser SSL implementations validate that your certificate is computationally secure, it says nothing about the path your cert takes to a root. If you go to facebook.com 10,000 times through one certificate path, and suddenly it changes, it may be worth investigating. 

I'm not really sure where to work in potentially every color in that space into a UI and make it look good, but that silly star that I never use could probs change colors.
