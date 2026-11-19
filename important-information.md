# Basic Information
<grapheme> (how it is written)
/phoneme/ (how it sounds)
* [IPA Chart](https://www.ipachart.com/)


# Normalization
You can read more about [unicode normalization](https://unicode.org/reports/tr15/#Norm_Forms)

We should use NFC for all applications. It is the correct choice because it decomposes and recomposes characters in a lossless way. 

For example, it is possible to have two characters that visually appear to be ř. However, that may not be the case, as there are 2 ways to represent this character: \u0159 (len is 1) and r\u030c (len is 2).

* NF**D** (Decomposition) will take both and turn them into the form r\u030c. 
* NF**C** (Composition) decomposes the same way NFD does, but then recomposes both into \u0159.

## What advantage does NFC have over NFD for our purposes?

Some characters can be stored in two ways. For example, ř can be one character (\u0159) or an r followed by a separate accent mark (r\u030c). They are meant to look the same, and on most modern software they do, but the computer treats them as different strings, so comparing them fails.

Normalization fixes this by converting all text to one agreed-upon spelling. NFC and NFD both do this safely: they only combine or split spellings that Unicode defines as the same character, so the meaning never changes. Either works as long as we use it consistently on everything (both the inventory and the input text).

We choose NFC because it is the common default. Most existing text is already NFC, it is shorter (ř is 1 character instead of 2), and when we later display characters, it will be more reliable: a single precomposed character has its accent placed by the font designer, while a separate accent has to be positioned by the software, and some fonts and programs do that badly, even rendering them in seperate boxes.

## What about NFKD and NFKC?

The K in these names refers to "compatibility" which would seem good, however, it is the lossy kind of compatibility, whereby 2⁵ → 25 (because the superscripting went away). 

This is particularly egregious in linguistics as "bʷ" will become "bw". In linguistics, "bʷ" means you put your lips in the "w" shape, and say /b/ (similarly, bʰ makes the /b/ sound with the puff of air like an h, and bʲ the tongue takes the "yod" shape). Therefore bw and bʷ are distinct sounds, and should not be mixed together.