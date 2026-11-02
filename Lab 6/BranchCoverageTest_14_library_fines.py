from library_fines import late_fine, can_borrow, renewal_status

# late_fine branches
def test_late_fine_branches():
    assert late_fine("student", 10, False) == 0
    assert late_fine("faculty", 35, False) == 5
    assert late_fine("student", 20, True) == 162
    assert late_fine("guest", 100, False) == 200

def test_late_fine_invalid_member():
    try:
        late_fine("unknown", 10, False)
        assert False
    except ValueError:
        pass

def test_late_fine_invalid_days():
    try:
        late_fine("student", -1, False)
        assert False
    except ValueError:
        pass

# can_borrow branches
def test_can_borrow_branches():
    assert can_borrow(1, 101, "student") is False
    assert can_borrow(5, 0, "faculty") is True
    assert can_borrow(10, 0, "faculty") is False
    assert can_borrow(2, 0, "student") is True
    assert can_borrow(3, 0, "student") is False

# renewal_status branches
def test_renewal_status_branches():
    assert renewal_status(0, True, 5) == "denied"
    assert renewal_status(2, False, 5) == "limit reached"
    assert renewal_status(0, False, -1) == "overdue"
    assert renewal_status(0, False, 5) == "renewed"