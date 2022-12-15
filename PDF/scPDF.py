#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ENKRIPSI


# In[8]:


from PyPDF2 import PdfFileWriter, PdfFileReader
  
# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf asli 
file = PdfFileReader('E:/tugas/UASPSKD/file_pdf.pdf')
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num):
    
   
    page = file.getPage(idx)
      

    out.addPage(page)
  
  
# masukkan password enkripsi 
password = "syahh229"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open('E:/tugas/UASPSKD/file_pdf.pdf', "wb") as f:
    
    # simpan pdf 
    out.write(f)


# In[ ]:


#DESKRIPSI


# In[9]:


from PyPDF2 import PdfFileWriter, PdfFileReader
  
# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf yg terenkripsi
file = PdfFileReader('E:/tugas/UASPSKD/file_pdf.pdf')
  
# masukkan password enkripsi 
password = "syahh229"
  
# cek file terenkripsi atau tidak 
if file.isEncrypted:
  
    # jika file terenkripsi, langsung di dekripsi pakai password 
    file.decrypt(password)
  
    # dekripsi dilakukan setiap halaman file pdf
    # simpan ke dalam file baru 
    for idx in range(file.numPages):
        
        # identifikasi halaman file 
        page = file.getPage(idx)
          
        # masukkan halaman yg sudah diidentifikasi dan sudah di dekripsi ke file baru 
        out.addPage(page)
      
    # buka file baru "myfile_decrypted.pdf"
    with open('E:/tugas/UASPSKD/file_pdf.pdf', "wb") as f:
        
        # simpan file baru 
        out.write(f)
  

    print("File decrypted Successfully.")
else:
    
    print("File already decrypted.")


# In[ ]:




