# xeople

Xeople is a simple people selector, made with python using random module.

## Usages

- First we need to prepare the files that contains people names. You could make
it by make a file that contains people names and divide it by using newline.

Example `people-names`:
```
Agil
Aisyah
Fia
Dias
Azizah
Damar
Diana
Dina
Fadia
Hilmy
Kiki
...
```

- To make an individiual select you could do:

```
./main.py <file that contains people names>
```

Example:
```
$ ./main.py people-names
Here is the lucky people who get selected: Hilmi
```

- To make group select you could do:
```
./main.py <file that contains people names> --group=<how many group will be created>
```

Example:
```
$ ./main.py test-name --group 8
========
GROUP 1
========
1. Dina
2. Fikra
3. Alif
4. Hanna
5. Rukha

========
GROUP 2
========
1. Rafid
2. Kiki
3. Fia
4. Tiara

========
GROUP 3
========
...
```

## Development

After cloning the repo, you could do `nosetests` to make sure all function works
normally.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rafidaslam/xeople/.

## License

`xeople` is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
