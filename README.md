Verify UUID
===========

    __     __                     __   ______                  __    __  __    __  ______  _______
    /  |   /  |                   /  | /      \                /  |  /  |/  |  /  |/      |/       \
    $$ |   $$ | ______    ______  $$/ /$$$$$$  |__    __       $$ |  $$ |$$ |  $$ |$$$$$$/ $$$$$$$  |
    $$ |   $$ |/      \  /      \ /  |$$ |_ $$//  |  /  |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
    $$  \ /$$//$$$$$$  |/$$$$$$  |$$ |$$   |   $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
     $$  /$$/ $$    $$ |$$ |  $$/ $$ |$$$$/    $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
      $$ $$/  $$$$$$$$/ $$ |      $$ |$$ |     $$ \__$$ |      $$ \__$$ |$$ \__$$ | _$$ |_ $$ |__$$ |
       $$$/   $$       |$$ |      $$ |$$ |     $$    $$ |      $$    $$/ $$    $$/ / $$   |$$    $$/
        $/     $$$$$$$/ $$/       $$/ $$/       $$$$$$$ |       $$$$$$/   $$$$$$/  $$$$$$/ $$$$$$$/
                                               /  \__$$ |
                                               $$    $$/
                                                $$$$$$/

**Verify UUID** is a tool written in Python for validating a UUID.

Valid UUIDs<br>
Output further information about the UUID, current version and variant.

Non-valid UUIDS<br>
If the UUID is incorrect, the cause of the error is determined.


A brief overview of usage
```
git clone ...
cd verify_uuid/src
pip3 install -r requirements.txt
python3 main.py -h
```

A detailed documentation is written with Sphinx, a build version available under `docs/build/html/index.html`.

----------

This project was also used to explore the topics of documentation, open source and testing in Python.
