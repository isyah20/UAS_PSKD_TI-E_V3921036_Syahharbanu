#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ENKRIPSI


# In[3]:


try : 
    path = input(r'Masukkan path image : ')#menambahkan path dari file gambar,'r' digunakan untuk membaca file pada disk
    key = int(input('Masukkan kunci enkripsi : ')) #menambahkan key untuk enkripsi
    
    
    print('path : ', path) #menampilkan path yang diinputkan
    print('key : ', key) #menampilkan key yang diinputkan
    
    fin = open(path, 'rb')#membuka file, 'rb' digunakan untuk menyatakan bahwa file dengan mode biner hendak dibaca.
    
    image = fin.read()#membaca data biner gambar
    fin.close()#menutup file 
    
    image = bytearray(image) #mengubah bentuk data biner menjadi array bite
    
    for index, values in enumerate(image):#menerapkan operasi XOR pada setiap nilai array bite supaya gambar tidak dapat dibuka
        image[index] = values ^ key
        
    fin = open(path, 'wb')#membuka file gambar yang sudah di XOR
    
    fin.write(image)#menyimpan gambar 
    fin.close()
    print('encryption done...')#ketika enkripsi berhasil diterapkan
    
    
except Exception:
    print('Error caught : ', Exception._name_)#ketika enkripsi tidak berhasil diterapkan


# In[ ]:


#DESKRIPSI


# In[4]:


try : 
    path = input(r'Masukkan path image : ')#menambahkan path dari file gambar,'r' digunakan untuk membaca file pada disk
    key = int(input('Masukkan kunci enkripsi : ')) #menambahkan key untuk enkripsi
    
    
    print('path : ', path) #menampilkan path yang diinputkan
    print('Note : kunci pada enkripsi dan deskripsi harus sama.')
    print('key : ', key) #menampilkan key yang diinputkan
    
    fin = open(path, 'rb')#membuka file, 'rb' digunakan untuk menyatakan bahwa file dengan mode biner hendak dibaca.
    
    image = fin.read()#membaca data biner gambar
    fin.close()#menutup file 
    
    image = bytearray(image) #mengubah bentuk data biner menjadi array bite
    
    for index, values in enumerate(image):#menerapkan operasi XOR pada setiap nilai array bite supaya gambar tidak dapat dibuka
        image[index] = values ^ key
        
    fin = open(path, 'wb')#membuka file gambar yang sudah di XOR
    
    fin.write(image)#menyimpan gambar 
    fin.close()
    print('descrytion done...')#ketika deskripsi berhasil diterapkan
    
    
except Exception:
    print('Error caught : ', Exception._name_)#ketika deskripsi tidak berhasil diterapkan


# In[ ]:





# In[ ]:




