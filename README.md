# PEB

All you need is to run:

```shell
git clone https://github.com/bound1ess/peb.git
./peb/app create --name my_first_ext
```

That will check your PHP-CPP installation, create a directory for your extension, 
copy all needed files and perform some required changes.
Next steps (building and installing your extension) will also be provided.

## Cement dependency

Here is what I did on *Ubuntu 14.04*:

```shell
sudo apt-get install pip3
pip3 install cement
python3
>>> from cement.core import foundation
```

## License 

MIT (see the `LICENSE` file).
