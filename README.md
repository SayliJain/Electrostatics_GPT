# Electrostatics_GPT
A simple Topic GPT model for Electrostatics

## Installing Python

1. **Open Windows Command Prompt**

2. **Check if Python is installed**
   
```
python --version
```

If Python is available, it will return the version of Python installed. If not, it will return "Python was not found."

In case an older version of Python is installed on your system (<3.11), upgrade it by installing the latest version from the Python website (version 3.11).

### 3. **Installing Python**

a. Download the Python installer from this [website](https://www.python.org/downloads/release/python-3114/).

b. Run the installer for Python 3.11 version for 64-bit Windows machine.

c. Click and check the checkboxes for:
   - Use admin privileges when installing py.exe
   - Add python.exe to PATH

d. Click on "Install Now"

e. If you encounter any trouble during installation, run the installer again with the same options but do a customized installation with the "Precompile standard library" option checked, or contact tech support if you are unable to install Python.

f. Restart the Command Prompt and check the Python version again by running:
   ```
   python --version
   ```
   This should return "3.11.4." If "Python was not found" is returned, restart the system and run `python --version` again.

## Downloading the Electrostatics Topic GPT Folder

1. Download the "Electrostatic_TopicGPT" zip folder from this repository or clone it on your computer using Git.
- Store it in a preferable place and remember its path (you can copy the path from the address bar).

2. Open the terminal on the path in which you have stored the Electrostatics folder or change the directory to your working directory using `cd <path>`.

3. On the command prompt, run the following commands one by one:

   ```
   python -m pip install --upgrade pip
   ```
   
   ```
   pip install update wheel
   ```


## Let's Start Building our Electrostatics Topic GPT

1. **First, install all the required libraries** using the following command:


   ```
   pip install torch numpy transformers datasets tiktoken wandb tqdm
   ```
   
   

2. **Prepare the dataset** by running the command:


   ```
   python data/electrostatics/prepare.py
   ```
- This splits the data into testing and validation and provides a data description:


```
length of dataset in characters: 847,513
all the unique characters: !"%&'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz|~¢¥®°±µ·ºÅÐ×æî÷üɵˆΔΣΦαδεθκλνοπρστφχḗἤ–—‘’“”•…′Ω→∆∑−√∝∞∫≅≥⊥⋅□ﬁﬂ
vocab size: 171
train has 762,761 tokens
val has 84,752 tokens
```


3. **Then, train the model on your device** using the following command:

- If you are using a CPU, run:

```
python train.py config/train_electrostatics_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```

- If you are using a GPU, run:

```
python train.py config/train_electrostatics_char.py 
```

- After running this command, If you get an error stating **"Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure."** Please install [Microsoft Visual C++ Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe). Run the file, then the error will be resolved. 

4. **Then, sample the data and print it**.

- The command for CPU:
   ```
   python sample.py --out_dir=out-electrostatics --device=cpu
   ```

- The command for GPU:
  
   ```
   python sample.py --out_dir=out-electrostatics 
   ```
   
- If you want to start generating data from a specific string of characters, use `--start="Enter string here"`:


    ```
    python sample.py --out_dir=out-electrostatics --device=cpu --start="Enter string here"
    ```

  




