Here are Built-in charsets;

?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?h = 0123456789abcdef
?H = 0123456789ABCDEF
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
?a = ?l?u?d?s
?b = 0x00 - 0xff

Example of usage custom charset;

hashcat -m 22000 hash.hc22000 -a3 -1 ?l?u?d ?1?1?1?1?1?1?1?1    // This special charset generates an 8-digit password in all combinations containing only lowercase letters, uppercase letters and numbers. 

hashcat -m 22000 hash.hc22000 -a3 -1 ?l?u?d?s ?1?1?1?1?1?1?1?1?1?1    // This special charset generates an 10-digit password in all combinations containing only lowercase letters, uppercase letters, numbets and special characters.
