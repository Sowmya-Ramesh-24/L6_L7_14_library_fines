from library_fines import late_fine, can_borrow, renewal_status

def test_late_fine():
    assert late_fine("student", 10, False) == 0
    assert late_fine("faculty", 35, False) == 5
    assert late_fine("guest", 20, True) == 180
    assert late_fine("guest", 100, False) == 200

def test_late_fine_errors():
    try:
        late_fine("unknown", 10, False)
        assert False
    except ValueError:
        pass

    try:
        late_fine("student", -1, False)
        assert False
    except ValueError:
        pass

def test_can_borrow():
    assert can_borrow(1, 0, "student") is True
    assert can_borrow(3, 0, "student") is False
    assert can_borrow(5, 0, "faculty") is True
    assert can_borrow(10, 0, "faculty") is False
    assert can_borrow(1, 101, "student") is False

def test_renewal_status():
    assert renewal_status(0, True, 5) == "denied"
    assert renewal_status(2, False, 5) == "limit reached"
    assert renewal_status(0, False, -1) == "overdue"
    assert renewal_status(0, False, 5) == "renewed"