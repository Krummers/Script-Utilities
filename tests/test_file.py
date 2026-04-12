import os
import pytest as pt

import script_utilities.file as fl

def test_initialisation():
    filename = "a.txt"
    path = os.path.join(os.getcwd(), filename)
    folder = os.getcwd()
    
    file = fl.File(path)
    
    assert file.path == path
    assert file.folder == folder
    assert file.filename == filename

def test_representation():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    assert repr(file) == path

def test_exists():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")

    assert bool(file)
    os.remove(path)

def test_rename():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    renamed_path = os.path.join(os.getcwd(), "b.txt")
    file.rename("b.txt")
    
    assert os.path.exists(renamed_path)
    os.remove(renamed_path)

def test_move():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    renamed_path = os.path.join(os.getcwd(), "test-move", "a.txt")
    file.move(renamed_path)
    
    assert os.path.exists(renamed_path)
    os.remove(renamed_path)
    os.rmdir(os.path.dirname(renamed_path))

def test_move_wrong_filename():
    with pt.raises(ValueError):
        path = os.path.join(os.getcwd(), "a.txt")
        file = fl.File(path)
        open(path, "x")
        
        renamed_path = os.path.join(os.getcwd(), "test-move", "b.txt")
        file.move(renamed_path)
    
    os.remove(path)

def test_move_down():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    renamed_path = os.path.join(os.getcwd(), "test-move-down", "1", "2", "a.txt")
    file.move_down(["test-move-down", "1", "2"])
    
    assert os.path.exists(renamed_path)
    os.remove(renamed_path)
    for _ in range(3):
        renamed_path = os.path.dirname(renamed_path)
        os.rmdir(renamed_path)

def test_move_down_without_creating_folders():
    with pt.raises(FileNotFoundError):
        path = os.path.join(os.getcwd(), "a.txt")
        file = fl.File(path)
        open(path, "x")
        
        file.move_down(["test-move-down", "1", "2"], create = False)
    
    os.remove(path)

def test_move_down_wrong_type():
    with pt.raises(TypeError):
        path = os.path.join(os.getcwd(), "a.txt")
        file = fl.File(path)
        open(path, "x")
        
        file.move_down("test-move-down", "1")
    
    os.remove(path)

def test_move_up():
    os.makedirs(os.path.join(os.getcwd(), "test-move-up", "1", "2"))
    path = os.path.join(os.getcwd(), "test-move-up", "1", "2", "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    renamed_path = os.path.join(os.getcwd(), "a.txt")
    file.move_up(3)
    
    assert os.path.exists(renamed_path)
    os.remove(renamed_path)
    for _ in range(3):
        path = os.path.dirname(path)
        os.rmdir(path)

def test_move_up_wrong_type():
    with pt.raises(TypeError):
        os.makedirs(os.path.join(os.getcwd(), "test-move-up", "1", "2"))
        path = os.path.join(os.getcwd(), "test-move-up", "1", "2", "a.txt")
        file = fl.File(path)
        open(path, "x")
        
        file.move_up([1, 2, 3])
    
    os.remove(path)
    for _ in range(3):
        path = os.path.dirname(path)
        os.rmdir(path)

def test_copy():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    new_path = os.path.join(os.getcwd(), "test-copy", "b.txt")
    file.copy(new_path)
    
    assert os.path.exists(path)
    assert os.path.exists(new_path)
    os.remove(path)
    os.remove(new_path)
    os.rmdir(os.path.dirname(new_path))

def test_delete():
    path = os.path.join(os.getcwd(), "a.txt")
    file = fl.File(path)
    open(path, "x")
    
    file.delete()
    
    assert not os.path.exists(path)

if __name__ == "__main__":
    os.system(f"pytest {os.path.basename(__file__)}")
