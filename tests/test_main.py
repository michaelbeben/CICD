import src.fizzbuzz

def test_fizz(capfd):
    src.fizzbuzz.fizzbuzz(4)
    out, err = capfd.readouterr()
    assert out == "FIZZ\n" 

def test_buzz(capfd):
    src.fizzbuzz.fizzbuzz(6)
    out, err = capfd.readouterr()
    assert out == "FIZZ\nBUZZ\n" 

def test_fizzbuzz(capfd):
    src.fizzbuzz.fizzbuzz(16)
    out, err = capfd.readouterr()
    assert out == "FIZZ\nBUZZ\nFIZZ\nFIZZ\nBUZZ\nFIZZ\nFIZZBUZZ\n" 