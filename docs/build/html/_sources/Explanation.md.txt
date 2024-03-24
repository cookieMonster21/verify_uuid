Explanation
===========

<!--- Referenzierung an anderen Positionen möglich, wird nicht angezeigt --->
(explanation)=

## Aim of UUIDs
- To ensure that information is reliably unique
- Used as identification number
- is considered universally unique - worldwide

## General Information
- **U**niversally **U**nique **Id**entifier (UUID)
- often also referred as **GUID** (**G**lobally **U**nique **Id**entifier)
- Defined in the standard [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122)
- 5 versions have been defined
- Format
  - 8-4-4-4-12 `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
  - each `x` is represented by a character from the hexadecimal system: `0-9`and `A-F`. 
  - Capitalization is not relevant.
- Version and Variant can be identified by a character on a specific position
  - Version (M)
  - Variant (N)
  - `xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx`
- Variants
  - RFC4122 UUID and Microsoft GUID are synonyms, same principle
  - Overview:

  | Hex Digest | Variant                                                                | Return Value from Software           |
  |------------|------------------------------------------------------------------------|--------------------------------------|
  | 0-7        | Backwards compatible with Apollo Network Computing, no longer relevant | reserved for NCS compatibility       |
  | 8-b        | RFC 4122/DCE 1.1; ISO/IEC 11578:1996                                   | specified in RFC 4122                |
  | c-d        | Microsoft GUID                                                         | reserved for Microsoft compatibility |
  | e          | future versions                                                        | reserved for future definition       |
  | f          | unknown, not valid                                                     | reserved for future definition       |



### Description of the versions
Following