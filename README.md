# unicode-string-contain-check
This python package is performing `in` with UTF-8 encoded to support non-Latin charathers including CJK language


|**Testing Language**|**Test result**|
|---|---|
|Chinese (Simp.)|<span style="color: lime">Passed</span>|
|Chinese (Trad.)|<span style="color: lime">Passed</span>|
|Japanese|<span style="color: lime">Passed</span>|
|Korean|<span style="color: lime">Passed</span>|

<br>

It should be fine for other language, otherwise, please create new issue to solving problem

<hr>

## Usage
Import this package first:
```python
import UnicodeStringContainCheck
```
Recommended ways:
```python
# Name what you want
import UnicodeStringContainCheck as uin
```
Check does the word contain in the phrase:
```python
if uin.utf_contain("遊戲保持了前作般的高自由度，玩家可以隨心所欲地進行","隨心所欲"):
    print("It's contain!!!")
```
The result wil be like this:
```
It's contain!!!
```
A python file should be looks like:
```python
import UnicodeStringContainCheck as uin

if __name__ == "__main__":
    if uin.utf_contain("遊戲保持了前作般的高自由度，玩家可以隨心所欲地進行","隨心所欲"):
        print("It's contain!!!")
```

<hr>

## Guides
`contain(usr_input,target_text)`: Check does the target (`target_text`) contains in a string (`usr_input`)

<hr>

## License

Apache 2.0