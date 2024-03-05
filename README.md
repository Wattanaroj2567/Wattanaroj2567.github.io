![banner](https://picsum.photos/800/250)

# สมุดบันทึก :atom: :dependabot:

## สำหรับรายวิชา [OOP](https://Wattanaroj2567.github.io)

![download.gif](./CatsLoveToGiveKissesToo (10 Gifs).gif)
 
#### วรรธนโรจน์ บุตรดี

### git config **(การกำหนดบันทึกไฟล์อัปโหลดจาก Vscode เข้าไปใน github)**
*  user.name ซึ่งกำหนดชื่อผู้ใช้ Git และ user.email ซึ่งกำหนดอีเมลของผู้ใช้ Git
~~~
git config --global user.name "wattanaroj2567"
git config --global user.email "wattanaroj.bu.66@ubu.ac.th"
~~~
*ดังนั้น คำสั่งที่ให้มาคือการกำหนดชื่อผู้ใช้ Git ของคุณเป็น "wattanaroj2567" และอีเมลของคุณเป็น "wattanaroj.bu.66@ubu.ac.th"
 ซึ่งจะถูกใช้เมื่อคุณทำการ commit ใน Git repository ใดๆ ที่คุณติดตั้งไว้ในระบบของคุณ*

### code
~~~
git status
git add
git commit
~~~
### คำสั่งพื้นฐาน python
~~~
python
d = {'frame': 4.00, 'bancha': 2.00}
for k,v in d.items():
   print(k,v)
~~~

### ***สิ่งที่เราควรทำ ก่อนเริ่ม Project (อธิบายโดยละเอียด!!) ก่อนอ่านดูดีๆนะครับเพื่อไม่ให้ต้องสับสน ทำได้แน่นอน 100% ผมลองทำมาหลายรอบแล้วได้ผลลัพธ์ที่ดี***

#### - **Open Program Vscode ขึ้นมาแล้ว** 

#### 0. กด Ctrl+Shift+P แล้วพิม Git clone แล้วนำลิงค์ไฟล์ Project ที่คุณสร้างไว้ของ Github มาวางในช่องค้นหา  **ยกตัวอย่างเช่น https://github.com/wattanaroj2567/wattanaroj2567.github.io**
#### 1. คำอธิบายเพิ่มเติมในส่วนของ git clone (***ขั้นตอนเหล่านี้ถ้าเรามี Git แล้วข้ามไปข้อที่ 2 ได้เลย***)  
  * Git clone คือของ Git ในการจะเอาลิงค์มาทำสำเนาต้องเป็น  Github ทำเพื่อสร้างสำเนานำเข้ามาในเครื่อง โดยไม่ต้องทำใน github โดยตรงก็ได้
  * ไม่ขึ้น Git clone ให้ไปคัดลอกโค้ดในเว็บไซต์ >> *scoop.sh* << แล้วมาวางใน *PowerShell เท่านั้น ห้าม Run as administartor เด็ดขาด เพราะเราจะเรียกผู้ดูแลระบบมาทำไมล่ะ เราแค่โหลดเฉยๆ* Enter เล๊ย
    
     ~~~
     - > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     - > Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
     ~~~
     
  * รอแปป ขึ้นงี้มา แต่เครื่องจะไม่เหมือนกัน >> *PS C:\Users\tawan> scoop insatall git* << เยี่ยมครับ คุณทำถูกแล้ว โหลดเสร็จแล้วล้าา ปิดโปรแกรม
  
#### 2. จะเด้งหน้าให้เลือกไฟล์ แนะนำให้เลือกไดร์ฟ D ดีกว่า หาไฟล์ง่ายดี ไม่มีไดร์ฟ D เอา C แทนได้ เพราะต้องใช้พื้นที่เยอะอยู่ สร้าง Folder ที่ต้องการ แค่นี้ก็จะเสร็จในส่วนของ Git clone นะครับ

#### 3. สร้างสภาพแวดล้อม (environment) 
 -- สร้างโฟลเดอร์สภาพแวดล้อมใหม่
 
   **a. venv**
   ```
   python -m venv myvenv
   ```
  **b. conda**
  ```
   conda create --name myvenv 
  ```
#### 4. เปิดใช้งานสภาพแวดล้อม (activate)
 -- การเปิดใช้งานโฟลเดอร์สภาพแวดล้อมที่เราได้สร้างขึ้นมา
 
  **a. venv**
  ```
  venv/scripts/activate 
  ```
  **b. conda**
  ```
  conda activate myvenv
  ```
#### 5. ติดตั้งแพ็คเกต (install package)
 -- ติดตั้งแพ็คเกตเข้าโฟลเดอร์สภาพแวดล้อม ***ย้ำ!! ระบุตัวแพ็คเกตให้ชัดเจนและถูกต้อง***
  ```
  pip install streamlit
  ```
#### 6. ในการรันเพื่อเข้าหน้าเว็บ เลื่อนดูด้านล่างสุดและต้องใช้ไฟล์ Python ที่ใช้รันนะ ***ห้าม!! กดเครื่องหมาย > ด้านขวาบน เด็ดขาด รันเข้าเว็บไม่ได้***
 -- ทำตามครบแบบนี้ก็เสร็จเป็นที่เรียบร้อยแล้วครับ ใช้งานได้เรื่อยๆ

### Conda Error 
 ปัญหาคือ คุณไม่ได้ติดตั้งยังไงล่ะ? ถ้าจำเป็นหรืออยากใช้เพื่อสร้างภาพแวลดล้อมทำได้ครับ อันนี้โครตเบิกกว้างอยู่ ใช้กับภาษาโปรแกรมอื่นๆได้  
 - Anaconda  >>> แพ็คเกตจะใหญ่กว่า miniconda หลายเท่ายังดีแถมโปรแกรม Python 3.11.5 มาด้วยกัน ไม่เสียเวลาโหลดแยก พร้อมโปรแกรมอื่นๆอย่าง Jupyter Vscode. เป็นโปรแกรมของ Anaconda สามารถเลือกติดตั้งได้เอง Download >> ( https://www.anaconda.com/download )
 - Miniconda >>> แพ็คเกตจะไม่ใหญ่มาก ต่างจาก Anaconda เยอะ แถมโปรแกรม Python 3.12.2 ตัวเดียว Download >> ( https://docs.anaconda.com/free/miniconda/ )


> [!NOTE]
> ก่อนอื่นแนะนำเลยนะ สร้างของ venv ดีกว่า มันมาพร้อม Windows เลย แต่ะจะเป็นได้แค่เฉพาะ Python เท่านั้น แต่ภาษาโปรแกรมอื่นๆ venv ไม่ได้นะจ๊ะ

 
 __Q&A__
 
 **[ถาม]** ทำไมต้องสร้างสภาพแวดล้อมด้วยล่ะ? ( ความคิดส่วนตัวผมที่ศึกษาคร่าวๆมา )
 
 **[ตอบ]** นั่นสิ แต่ว่าๆมันมีประโยชน์โครตๆเลยอ่ะ มีความารถก็คือ เก็บแพ็คเกตที่เราติดตั้งไว้ เข้าไปในโฟลเดอร์ของสภาพแวดล้อม แถมยังรักษาข้อมูลที่เราติดตั้งเอาไว้ใช้ได้ยาวๆด้วยแหละ


## Streamlit
### install ติดตั้งเหมือนกัน

 **a. venv install [package]** 
 ```
   pip install streamlit 
 ```
 **b. conda install [package]** 
 ```
   conda install streamlit  
 ```
  
### uninstall แตกต่างกัน

 **a. venv uninstall [package]**
 ```
   pip uninstall streamlit 
 ```
 **b. conda uninstall [package]**
 ```
   conda remove streamlit 
 ```
 
### update and upgrade  แตกต่างกัน

 **a. venv upgrade [package]** 
 ```
   pip install --upgrade streamlit 
 ```
 **b. conda update [package]**
 ```
   conda update streamlit 
 ```

 
## Diffusers
  **ได้ครบที่ต้องการ ไม่ต้อง install diffusers ตัวเดียวเพิ่ม นี่คือตัวติดตั้งแพ็คเกตเสริมเพิ่มเติม เผื่อติดตั้ง diffusers ตัวเดียว แล้วไม่มี**
 
 **a. venv upgrade[package]** 
 ```
   pip install --upgrade diffusers[torch]
 ```
 ```
   pip install --upgrade transformers
 ```
**b. conda update[package]**
 ```
   conda update diffusers[torch]
 ```
 ```
   conda update transformers
 ```

   > [!TIP]
   > 1. python pygame/app01.py
   > 2. python pyside6/app01.py
   > 3. streamlit run streamlit/app01.py
   > 4. python diffusers/app01.py

