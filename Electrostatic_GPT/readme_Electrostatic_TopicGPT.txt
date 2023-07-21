1.Open Windows Command Prompt
2.Check if python is installed
	a.>python --version
	If python is available, it will return the version of python installed
        If python is not available, it will return "Python was not found" 
	b. If there is an older version installed (<3.11), upgrade it by installing latest version:    

3. Installing Python 
	a. Download python installer from :https://www.python.org/downloads/release/python-3114/
	b. Run the Installer for the python 3.11 version for 64 bit windows machine.
        c. Click and Check the checkboxes for 
		Use admin privileges when installing py.exe
                Add python.exe to PATH
        d.Click on Install Now 
        e.If there is any trouble encountered during installation:
		Again run the installer this time same as above but do a custamized installation:
 			with Precompile standard library option checked
		Or Contact Tech-Support if unable to install python
	f.Then restart the command Prompt and check for the version of python by running 
	>python --version
	this should return 3.11.4
	If "Python was not found" is returned, then restart the system and run >python --version again

3. Download the Electrostatic_TopicGPT zip folder from the link:
   and store it in a preferable place,remember its path (you can copy the path from the address bar)
4. Open terminal on the path in which you have stored the nanogpt folder or
   Change the directory to your working direct using cd <path>	
5. On the command prompt run the following commands one by one:
        >python -m pip install --upgrade pip
        >pip install update wheel
	>pip install torch numpy transformers datasets tiktoken wandb tqdm
6. Prepare the dataset by running the command
	>python data/shakespeare_char/prepare.py
7. Then run the command to train your model
	>python train.py config/train_electrostatic_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
8. Then sample the data and print 
        >python sample.py --out_dir=out-electrostatic-char --device=cpu



# Electrostatics_GPT
A simple Topic GPT model for Electrostatics

## Installing Python

1. **Open Windows Command Prompt**

2. **Check if Python is installed**
   
```
python --version
```

If Python is available, it will return the version of Python installed
If Python is not available, it will return "Python was not found" 

If there is an older version installed (<3.11), upgrade it by installing the latest version from the python website (3.11)   

3. Installing Python


	a. Download python installer from this [website](https://www.python.org/downloads/release/python-3114/)

	b. Run the Installer for the python 3.11 version for 64-bit Windows machine.

  c. Click and Check the checkboxes for
     Use admin privileges when installing py.exe
     Add python.exe to PATH 


 
    
  d. Click on Install Now 
  
  
  e. If there is any trouble encountered during installation
  
Again run the installer the same as above but do a customized installation:
with Precompile standard library option checked
Or Contact Tech-Support if unable to install python

f.Then restart the Command Prompt and check for the version of Python by running 
```
python --version
```
This should return 3.11.4
If "Python was not found" is returned, then restart the system and run >python --version again


### Dowloading the Electrostatics Topic GPT Folder



1. Download the Electrostatic_TopicGPT zip folder from this repository or clone it on your computer using Git
   

Store it in a preferable place, and remember its path (you can copy the path from the address bar)


2. Open terminal on the path in which you have stored the Electrostatics folder or
   
   
Change the directory to your working direct using cd <path>	

 
3. On the command prompt run the following commands one by one:
   ```
   python -m pip install --upgrade pip
   ```
   
   ```
   pip install update wheel
   ```
   
### Lets start building our Electrostatics Topic GPT


1. First Install all the required libraries using the following command
   

   ```
   pip install torch numpy transformers datasets tiktoken wandb tqdm
   ```
   
   
3. Prepare the dataset by running the command
   

   ```
   python data/electrostatics/prepare.py
   ```


   This splits the data into testing and validation and provides a data description
   

```
length of dataset in characters: 847,513
all the unique characters: !"%&'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz|~¢¥®°±µ·ºÅÐ×æî÷üɵˆΔΣΦαδεθκλνοπρστφχḗἤ–—‘’“”•…′Ω→∆∑−√∝∞∫≅≥⊥⋅□ﬁﬂ
vocab size: 171
train has 762,761 tokens
val has 84,752 tokens
```
   
4. Then train the model on you device using the following command

**If you are using a CPU run:**

```
python train.py config/train_electrostatics_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```


**If you are using a GPU run:**

```
python train.py config/train_electrostatics_char.py 
```


5. Then sample the data and print it

   The command for CPU:
   
   ```
   python sample.py --out_dir=out-electrostatics --device=cpu
   ```

  The Command for GPU:

   ```
   python sample.py --out_dir=out-electrostatics 
   ```

  If you want to start generating data from a specific string of charcaters, use  --start="Enter string here"

    ```
    python sample.py --out_dir=out-electrostatics --device=cpu --start="Enter string here"
    ```

  





  

 
	
