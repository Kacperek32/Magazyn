import logging
logging.basicConfig(level=logging.DEBUG)

command = input("Co chciałbyś zrobić? ")
if command in ("exit"):
    if command == "exit":
     logging.info("Dzięki wielkie, do zobaczenia!")
    exit()

items = {"kebab", "pizza", "makaron", "burger"}