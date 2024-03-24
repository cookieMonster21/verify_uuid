How To Guides
=============

<!--- Referenzierung an anderen Positionen möglich, wird nicht angezeigt --->
(howto)=

### Example UUIDs
In all How To Guides the following UUIDs are used as example
- 77ec999b-d287-4268-9915-81d6c79a70ed
- 8c7b779c-c7f4-4fc1-8bc1-20a4b34d9028

### How do I verify a UUID?
```
python3 main.py --uuid=77ec999b-d287-4268-9915-81d6c79a70ed
```

### How do I verify several UUIDs at once?
1. Create a text file, e.g. `uuid_list.txt` and paste all UUIDs you want to verify line per line to the file.
Example:
```
77ec999b-d287-4268-9915-81d6c79a70ed
8c7b779c-c7f4-4fc1-8bc1-20a4b34d9028
```
2. Save the created file in the `path-to-tool/verify_uuid/src/` folder.
3. Execute command:
```
python3 main.py --list=uuid_list.txt
```