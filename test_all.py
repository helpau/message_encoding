def test_manchester():
    import manchester
    assert manchester.encode("0")=="01"
    assert manchester.encode("00000000")=="0101010101010101"
    assert manchester.encode("11111111")=="1010101010101010"
    assert manchester.encode("0011010111111101")=="01011010011001101010101010100110"

def test_nrz():
    import nrz
    assert nrz.encode("0")=="0"
    assert nrz.encode("0110")=="0110"

def test_bipolar_ami():
    import bipolar_ami
    assert bipolar_ami.encode("000")=="000"
    assert bipolar_ami.encode("0101")=="010-"
    assert bipolar_ami.encode("111")=="1-1"

def test_nrzi():
    import nrzi
    assert nrzi.encode("000")=="000"
    assert nrzi.encode("111")=="101"
    assert nrzi.encode("0101000")=="0110000"

def test_ec_4b5b():
    import ec_4b5b
    assert ec_4b5b.encode("0000")=="11110"
    assert ec_4b5b.encode("11001011")=="1101010111"

def test_scramble_3_5():
    import scramble_3_5
    scramble_3_5.encode("110110000001")=="110001101111"
