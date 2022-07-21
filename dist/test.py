from queue_l import isfloat,extract_from_the_queue,clear_queue,insert_to_the_queue
from binary_search import binary_search
from grouping import count

def test_answer():
    assert isfloat('3.5') == True

def test_number():
    assert binary_search([1,2,3,4,5],2) == True

def test_extract_empty():
    clear_queue()
    assert extract_from_the_queue() == None

def test_insert_queue():
    insert_to_the_queue('1')
    v=extract_from_the_queue()
    assert v==1

def test_grouping():
    assert count([7,1,2,1]) == {7:1,1:2,2:1}
