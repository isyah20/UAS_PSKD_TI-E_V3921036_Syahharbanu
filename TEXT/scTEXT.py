#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ENKRIPSI


# In[1]:


try : 
    path = input(r'Masukkan path text : ')#menambahkan path dari file text,'r' digunakan untuk membaca file pada disk
    key = int(input('Masukkan kunci enkripsi : ')) #menambahkan key untuk enkripsi
    
    
    print('path : ', path) #menampilkan path yang diinputkan
    print('key : ', key) #menampilkan key yang diinputkan
    
    fin = open(path, 'rb')#membuka file, 'rb' digunakan untuk menyatakan bahwa file dengan mode biner hendak dibaca.
    
    text = fin.read()#membaca data biner text
    fin.close()#menutup file 
    
    text = bytearray(text) #mengubah bentuk data biner menjadi array bite
    
    for index, values in enumerate(text):#menerapkan operasi XOR pada setiap nilai array bite supaya text tidak dapat dibuka
        text[index] = values ^ key
        
    fin = open(path, 'wb')#membuka file text yang sudah di XOR
    
    fin.write(text)#menyimpan text
    fin.close()
    print('encryption done...')#ketika enkripsi berhasil diterapkan
    
    
except Exception:
    print('Error caught : ', Exception._name_)#ketika enkripsi tidak berhasil diterapkan


# In[ ]:


#DESKRIPSI


# In[2]:


try : 
    path = input(r'Masukkan path text : ')#menambahkan path dari file text,'r' digunakan untuk membaca file pada disk
    key = int(input('Masukkan kunci enkripsi : ')) #menambahkan key untuk enkripsi
    
    
    print('path : ', path) #menampilkan path yang diinputkan
    print('Note : kunci pada enkripsi dan deskripsi harus sama.')
    print('key : ', key) #menampilkan key yang diinputkan
    
    fin = open(path, 'rb')#membuka file, 'rb' digunakan untuk menyatakan bahwa file dengan mode biner hendak dibaca.
    
    text = fin.read()#membaca data biner text
    fin.close()#menutup file 
    
    text = bytearray(text) #mengubah bentuk data biner menjadi array bite
    
    for index, values in enumerate(text):#menerapkan operasi XOR pada setiap nilai array bite supaya text tidak dapat dibuka
        text[index] = values ^ key
        
    fin = open(path, 'wb')#membuka file text yang sudah di XOR
    
    fin.write(text)#menyimpan text 
    fin.close()
    print('descrytion done...')#ketika deskripsi berhasil diterapkan
    
    
except Exception:
    print('Error caught : ', Exception._name_)#ketika deskripsi tidak berhasil diterapkan


# In[ ]:




