
import pytest, os

import temperature_plotting as tpl


def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10, 10])
    assert calc == 0
    
    calc = tpl.compute_mean([0, 10, 0])
    assert round(calc, 4) == 3.3333
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a", "b", "c"])
        
    calc = tpl.compute_mean([])
    assert calc == None


@pytest.mark.skip(reason="Test is bad")
def test_create_name_bad():  
    fname = tpl.create_name(456)
    assert fname == "plot_123.png"



def test_create_name():
    fname = tpl.create_name(123)
    assert fname == "plot_123.png"
    
    fname = tpl.create_name(-123)
    assert fname == None
    
    fname = tpl.create_name(None)
    assert fname == None



# integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")


