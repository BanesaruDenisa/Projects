import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


root = Tk()
root.geometry("300x200")

# combo
l1 = ttk.Label(root, text="Select the Table :",
               font=("Times New Roman", 14)).grid(column=0,
                                                  row=0, padx=25, pady=3)




tables = ["Producator", "Aprovizionare", "Factura_A", "Cosmetice",
          "Factura_C", "Comanda", "Angajat", "Transport", "Magazin"]

cmb = ttk.Combobox(root, values=tables, width=30)
cmb.grid(column=0, row=1, padx=10, pady=0)
cmb.current(0)



def opt():
    if cmb.get() == "Producator":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['CUI'])
            e2.insert(0, select['denumire'])
            e3.insert(0, select['brand'])
            e4.insert(0, select['localitate'])
            e5.insert(0, select['strada'])

        def Add():
            prodCUI = e1.get()
            proddenumire = e2.get()
            prodbrand = e3.get()
            prodloc = e4.get()
            prodstr = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  producator (CUI,denumire,brand,localitate, strada) VALUES (%s, %s, %s, %s, %s)"
                val = (prodCUI, proddenumire, prodbrand, prodloc, prodstr)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Producator inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            prodCUI = e1.get()
            proddenumire = e2.get()
            prodbrand = e3.get()
            prodloc = e4.get()
            prodstr = e5.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  producator set denumire= %s,brand= %s,localitate= %s, strada= %s where CUI= %s"
                # val = (prodCUI, proddenumire, prodbrand, prodloc, prodstr)
                update = "Update  producator set denumire= '%s',brand= '%s',localitate= '%s', strada= '%s' where CUI= '%s'" % (
                    prodCUI, proddenumire, prodbrand, prodloc, prodstr)
                mycursor.execute(update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            prodCUI = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from producator where CUI = %s"
                val = (prodCUI,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()



        # def sort():
        #     mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
        #                                       database="depozit")
        #     mycursor = mysqldb.cursor()
        #
        #     sor = ttk.Combobox(root, width="12", values=("CUI", "denumire", "brand", "localitate", "strada")).place(
        #         x=800, y=150)
        #
        #     sor = ttk.Label(root, text="Select the field :", font=("Times New Roman", 14)).grid(column=0,
        #                                                                                         row=1, padx=800,
        #                                                                                         pady=100)
        #
        #     if sor.get() == "CUI":
        #         mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
        #                                           database="depozit")
        #         mycursor = mysqldb.cursor()
        #         mycursor.execute("SELECT *  FROM producator order by CUI")
        #         lastid = mycursor.lastrowid
        #         messagebox.showinfo("information", "Sorted successfully")
        #         records = mycursor.fetchall()
        #         print(records)
        #
        #         for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
        #             listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
        #             mysqldb.close()
        #
        #     if sor.get() == "denumire":
        #
        #         mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
        #                                           database="depozit")
        #         mycursor = mysqldb.cursor()
        #         mycursor.execute("SELECT *  FROM producator order by denumire")
        #         records = mycursor.fetchall()
        #         print(records)
        #
        #         for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
        #             listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
        #             mysqldb.close()
        #
        #     if sor.get() == "brand":
        #
        #         mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
        #                                           database="depozit")
        #         mycursor = mysqldb.cursor()
        #         mycursor.execute("SELECT *  FROM producator order by brand")
        #         records = mycursor.fetchall()
        #         print(records)
        #
        #         for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
        #             listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
        #             mysqldb.close()

        # sor.place(relx="0.4", rely="0.1")
        # sor.grid(column=0, row=1, padx=800, pady=80)
        # buton = ttk.Button(root, text="sorteaza", command=sorteaza)
        # buton.place(x=800, y=200)

        def sortcui():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM producator ORDER BY CUI")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()

        def sortdenum():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM producator ORDER BY denmire")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()


        def sortbrand():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM producator ORDER BY brand")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()

        def sortloc():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM producator ORDER BY localitate")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()

        def sortstr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM producator ORDER BY strada")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()


        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT CUI, denumire, brand, localitate, strada FROM producator")
            records = mycursor.fetchall()
            print(records)

            for i, (CUI, denumire, brand, localitate, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(CUI, denumire, brand, localitate, strada))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6

        tk.Label(root, text="Tabel PRODUCATOR", fg="blue", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="CUI:").place(x=30, y=100)
        Label(root, text="Denumire:").place(x=30, y=140)
        Label(root, text="Brand:").place(x=30, y=180)
        Label(root, text="Localitatea:").place(x=30, y=220)
        Label(root, text="Strada:").place(x=30, y=260)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort CUI", command=sortcui, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort denumire", command=sortdenum, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort brand", command=sortbrand, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort localitate", command=sortloc, height=3, width=13).place(x=800, y=100)
        Button(root, text="Sort strada", command=sortstr, height=3, width=13).place(x=800, y=170)


        cols = ('CUI', 'denumire', 'brand', 'localitate', 'strada')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        # sort()
        listBox.bind('<Double-Button-1>', GetValue)


    elif cmb.get() == "Aprovizionare":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['nr_comanda_a'])
            e2.insert(0, select['CUI'])
            e3.insert(0, select['data_primire'])

        def Add():
            aprnr = e1.get()
            aprCUI = e2.get()
            aprdata = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  aprovizionare (nr_comanda_a, CUI, data_primire) VALUES (%s, %s, %s)"
                val = (aprnr, aprCUI, aprdata)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Aprovizinare inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            aprnr = e1.get()
            aprCUI = e2.get()
            aprdata = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:

                update = "Update  aprovizionare set CUI= '%s', data_primire= '%s' where nr_comanda_a= '%s'" % (
                    aprnr, aprCUI, aprdata)
                mycursor.execute(update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            aprnr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from aprovizionare where nr_comanda_a = %s"
                val = (aprnr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM aprovizionare ORDER BY nr_comanda_a")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_a, CUI, data_primire) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_a, CUI, data_primire))
                mysqldb.close()

        def sortcui():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM aprovizionare ORDER BY CUI")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_a, CUI, data_primire) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_a, CUI, data_primire))
                mysqldb.close()


        def sortdata():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM aprovizionare ORDER BY data_primire")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_a, CUI, data_primire) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_a, CUI, data_primire))
                mysqldb.close()


        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT nr_comanda_a, CUI, data_primire FROM aprovizionare")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_a, CUI, data_primire) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_a, CUI, data_primire))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel APROVIZIONARE", fg="green", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Numar comanda:").place(x=30, y=100)
        Label(root, text="CUI:").place(x=30, y=140)
        Label(root, text="Data primire:").place(x=30, y=180)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple",height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort nr_com", command=sortnr, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort CUI", command=sortcui, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort data", command=sortdata, height=3, width=13).place(x=650, y=240)

        cols = ('nr_comanda_a', 'CUI', 'data_primire')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)


    elif cmb.get() == "Cosmetice":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_produs'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['categorie'])
            e4.insert(0, select['stoc'])
            e5.insert(0, select['pret_unit'])
            e6.insert(0, select['data_expirare'])

        def Add():
            cosid = e1.get()
            cosnume = e2.get()
            coscat = e3.get()
            cosstoc = e4.get()
            cospret = e5.get()
            cosdata = e6.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  cosmetice (id_produs, nume, categorie, stoc, pret_unit, data_expirare) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (cosid, cosnume, coscat, cosstoc, cospret, cosdata)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Product inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            cosid = e1.get()
            cosnume = e2.get()
            coscat = e3.get()
            cosstoc = e4.get()
            cospret = e5.get()
            cosdata = e6.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  cosmetice set nume= %s,categorie= %s,stoc= %s, data_expirare= %s where id_produs= %s, pret_unit= %s"
                val = (cosid, cosnume, coscat, cosstoc, cospret, cosdata)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            cosid = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from cosmetice where id_produs= %s"
                val = (cosid,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()


        def having():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT categorie, count(id_produs) as nr"
                             " FROM cosmetice Group by  categorie Having categorie = 'fata'")
            records = mycursor.fetchall()
            print(records)

            for i, (categorie, nr) in enumerate(records, start=1):
                listBox.insert("", "end", values=(categorie, nr))
                mysqldb.close()


        def sortprt():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM cosmetice ORDER BY pret_unit")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()

        def sortstc():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM cosmetice ORDER BY stoc")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()

        def sortnum():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM cosmetice ORDER BY nume")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()

        def sortcat():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM cosmetice ORDER BY categorie")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()

        def sortdata():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM cosmetice ORDER BY data_expirare")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()


        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_produs, nume, categorie, stoc, pret_unit, data_expirare FROM cosmetice")
            records = mycursor.fetchall()
            print(records)

            for i, (id_produs, nume, categorie, stoc, pret_unit, data_expirare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_produs, nume, categorie, stoc, pret_unit, data_expirare))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel COSMETICE", fg="magenta", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Id produs:").place(x=30, y=100)
        Label(root, text="Nume:").place(x=30, y=140)
        Label(root, text="Categorie:").place(x=30, y=180)
        Label(root, text="Stoc:").place(x=30, y=220)
        Label(root, text="Pret/unitate:").place(x=30, y=260)
        Label(root, text="Data expirare:").place(x=30, y=300)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)

        e6 = Entry(root)
        e6.place(x=170, y=300)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Having", command=having, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort pret", command=sortprt, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort stoc", command=sortstc, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort nume", command=sortnum, height=3, width=13).place(x=800, y=100)
        Button(root, text="Sort categorie", command=sortcat, height=3, width=13).place(x=800, y=170)
        Button(root, text="Sort data", command=sortdata, height=3, width=13).place(x=800, y=240)

        cols = ('id_produs', 'nume', 'categorie', 'stoc', 'pret_unit', 'data_expirare')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=380)

        show()
        listBox.bind('<Double-Button-1>', GetValue)



    elif cmb.get() == "Factura_A":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['nr_crt_a'])
            e2.insert(0, select['nr_comanda_a'])
            e3.insert(0, select['id_produs'])
            e4.insert(0, select['cantitate'])
            e5.insert(0, select['pret_unit'])

        def Add():
            fanr = e1.get()
            facom = e2.get()
            faid = e3.get()
            facan = e4.get()
            fapret = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  factura_a (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) VALUES (%s, %s, %s, %s, %s)"
                val = (fanr, facom, faid, facan, fapret)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Factura_A inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            fanr = e1.get()
            facom = e2.get()
            faid = e3.get()
            facan = e4.get()
            fapret = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  factura_a set nr_comanda_a= %s,id_produs= %s, cantitate= %s, pret_unit= %s where nr_crt_a= %s"
                val = (fanr, facom, faid, facan, fapret)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            fanr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from factura_a where nr_crt_a= %s"
                val = (fanr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_a ORDER BY nr_comanda_a")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortid():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_a ORDER BY id_produs")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortcant():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_a ORDER BY cantitate")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortpret():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_a ORDER BY pret_unit")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit))
                mysqldb.close()


        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit FROM factura_a")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_a, nr_comanda_a, id_produs, cantitate, pret_unit))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel FACTURA_A", fg="black", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Numar curent:").place(x=30, y=100)
        Label(root, text="Nr comanda:").place(x=30, y=140)
        Label(root, text="Id produs:").place(x=30, y=180)
        Label(root, text="Cantitate:").place(x=30, y=220)
        Label(root, text="Pret/unitate:").place(x=30, y=260)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort nr_com", command=sortnr, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort id_produs", command=sortid, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort cantitate", command=sortcant, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort pret", command=sortpret, height=3, width=13).place(x=800, y=100)


        cols = ('nr_crt_a', 'nr_comanda_a', 'id_produs', 'cantitate', 'pret_unit')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)


    elif cmb.get() == "Factura_C":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['nr_crt_c'])
            e2.insert(0, select['nr_comanda_c'])
            e3.insert(0, select['id_produs'])
            e4.insert(0, select['cantitate'])
            e5.insert(0, select['pret_unit'])

        def Add():
            fcnr = e1.get()
            fccom = e2.get()
            fcid = e3.get()
            fccan = e4.get()
            fcpret = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  factura_c (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) VALUES (%s, %s, %s, %s, %s)"
                val = (fcnr, fccom, fcid, fccan, fcpret)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Factura_C inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            fcnr = e1.get()
            fccom = e2.get()
            fcid = e3.get()
            fccan = e4.get()
            fcpret = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  factura_c set nr_comanda_c= %s,id_produs= %s, cantitate= %s, pret_unit= %s where nr_crt_c= %s"
                val = (fcnr, fccom, fcid, fccan, fcpret)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            fcnr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from factura_c where nr_crt_c= %s"
                val = (fcnr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_c ORDER BY nr_comanda_c")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortid():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_c ORDER BY id_produs")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortcant():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_c ORDER BY cantitate")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def sortpret():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM factura_c ORDER BY pret_unit")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit))
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit FROM factura_c")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_crt_c, nr_comanda_c, id_produs, cantitate, pret_unit))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel FACTURA_C", fg="black", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Numar curent:").place(x=30, y=100)
        Label(root, text="Nr comanda:").place(x=30, y=140)
        Label(root, text="Id produs:").place(x=30, y=180)
        Label(root, text="Cantitate:").place(x=30, y=220)
        Label(root, text="Pret/unitate:").place(x=30, y=260)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)


        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort nr_com", command=sortnr, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort id_produs", command=sortid, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort cantitate", command=sortcant, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort pret", command=sortpret, height=3, width=13).place(x=800, y=100)

        cols = ('nr_crt_c', 'nr_comanda_c', 'id_produs', 'cantitate', 'pret_unit')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)

    elif cmb.get() == "Comanda":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)

            e1.insert(0, select['nr_comanda_c'])
            e2.insert(0, select['data_plasare'])
            e3.insert(0, select['data_expediere'])
            e4.insert(0, select['id_magazin'])
            e5.insert(0, select['nr_masina'])
            e6.insert(0, select['id_angajat'])

        def Add():
            comnr = e1.get()
            comdp = e2.get()
            comde = e3.get()
            comm = e4.get()
            commas = e5.get()
            comang = e6.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  comanda (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (comnr, comdp, comde, comm, commas, comang)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Product inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            comnr = e1.get()
            comdp = e2.get()
            comde = e3.get()
            comm = e4.get()
            commas = e5.get()
            comang = e6.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  comanda set data_plasare= %s,data_expediere= %s, id_magazin= %s, nr_masina= %s, id_angajat= %s where nr_comanda_c= %s"
                val = (comnr, comdp, comde, comm, commas, comang)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            comnr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from comanda where nr_comanda_c= %s"
                val = (comnr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()


        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY nr_comanda_c")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()


        def sortdatapls():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY data_plasare")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()


        def sortdataexp():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY data_expediere")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()

        def sortidmag():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY id_magazin")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()

        def sortnrmas():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY nr_masina")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()

        def sortang():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM comanda ORDER BY id_angajat")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute(
                "SELECT nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat FROM comanda")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat) in enumerate(records,
                                                                                                                start=1):
                listBox.insert("", "end",
                               values=(nr_comanda_c, data_plasare, data_expediere, id_magazin, nr_masina, id_angajat))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel COMANDA", fg="red", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Numar comanda:").place(x=30, y=100)
        Label(root, text="Data plasare:").place(x=30, y=140)
        Label(root, text="Data expediere:").place(x=30, y=180)
        Label(root, text="Id magazin:").place(x=30, y=220)
        Label(root, text="Numar masina:").place(x=30, y=260)
        Label(root, text="Id angajat:").place(x=30, y=300)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)

        e6 = Entry(root)
        e6.place(x=170, y=300)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort nr_com", command=sortnr, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort data_plasare", command=sortdatapls, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort data_expediere", command=sortdataexp, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort id_magazin", command=sortidmag, height=3, width=13).place(x=800, y=100)
        Button(root, text="Sort nr_masina", command=sortnrmas, height=3, width=13).place(x=800, y=170)
        Button(root, text="Sort id_angajat", command=sortang, height=3, width=13).place(x=800, y=240)

        cols = ('nr_comanda_c', 'data_plasare', 'data_expediere', 'id_magazin', 'nr_masina', 'id_angajat')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)


    elif cmb.get() == "Angajat":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)

            e1.insert(0, select['id_angajat'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['prenume'])

        def Add():
            angid = e1.get()
            angnum = e2.get()
            angpre = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  angajat (id_angajat, nume, prenume) VALUES (%s, %s, %s)"
                val = (angid, angnum, angpre)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Angajat inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            angid = e1.get()
            angnum = e2.get()
            angpre = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  angajat set nume= %s,prenume= %s where id_angajat= %s"
                val = (angid, angnum, angpre)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            angid = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from angajat where id_angajat= %s"
                val = (angid,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortang():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM angajat ORDER BY id_angajat DESC")
            records = mycursor.fetchall()
            print(records)

            for i, (id_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_angajat, nume, prenume))
                mysqldb.close()

        def sortnum():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM angajat ORDER BY nume")
            records = mycursor.fetchall()
            print(records)

            for i, (id_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_angajat, nume, prenume))
                mysqldb.close()

        def sortprenu():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM angajat ORDER BY prenume")
            records = mycursor.fetchall()
            print(records)

            for i, (id_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_angajat, nume, prenume))
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_angajat, nume, prenume FROM angajat")
            records = mycursor.fetchall()
            print(records)

            for i, (id_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_angajat, nume, prenume))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel ANGAJAT", fg="cyan", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Id angajat:").place(x=30, y=100)
        Label(root, text="Nume:").place(x=30, y=140)
        Label(root, text="Prenume:").place(x=30, y=180)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort id_angajat", command=sortang, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort nume", command=sortnum, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort prenume", command=sortprenu, height=3, width=13).place(x=650, y=240)


        cols = ('id_angajat', 'nume', 'prenume')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)


    elif cmb.get() == "Magazin":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)

            e1.insert(0, select['id_magazin'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['localitate'])
            e4.insert(0, select['strada'])
            e5.insert(0, select['numar'])

        def Add():
            magid = e1.get()
            magnum = e2.get()
            magloc = e3.get()
            magstr = e4.get()
            magnr = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  magazin (id_magazin, nume, localitate, strada, numar) VALUES (%s, %s, %s, %s, %s)"
                val = (magid, magnum, magloc, magstr, magnr)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Magazin inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            magid = e1.get()
            magnum = e2.get()
            magloc = e3.get()
            magstr = e4.get()
            magnr = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  magazin set nume= %s,localitate= %s, strada=%s, numar=%s where id_magazin= %s"
                # val = (magid, magnum, magloc, magstr, magnr)
                update = "Update  magazin set nume= '%s',localitate= '%s', strada='%s', numar='%s' where id_magazin= '%s'" % (
                    magid, magnum, magloc, magstr, magnr)
                mycursor.execute(update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            transnr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from magazin where id_magazin= %s"
                val = (transnr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortid():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM magazin ORDER BY id_magazin DESC")
            records = mycursor.fetchall()
            print(records)

            for i, (id_magazin, nume, localitate, strada, numar) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_magazin, nume, localitate, strada, numar))
                mysqldb.close()

        def sortnum():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM magazin ORDER BY nume")
            records = mycursor.fetchall()
            print(records)

            for i, (id_magazin, nume, localitate, strada, numar) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_magazin, nume, localitate, strada, numar))
                mysqldb.close()

        def sortloc():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM magazin ORDER BY localitate")
            records = mycursor.fetchall()
            print(records)

            for i, (id_magazin, nume, localitate, strada, numar) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_magazin, nume, localitate, strada, numar))
                mysqldb.close()

        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM magazin ORDER BY numar")
            records = mycursor.fetchall()
            print(records)

            for i, (id_magazin, nume, localitate, strada, numar) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_magazin, nume, localitate, strada, numar))
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_magazin, nume, localitate, strada, numar FROM magazin")
            records = mycursor.fetchall()
            print(records)

            for i, (id_magazin, nume, localitate, strada, numar) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_magazin, nume, localitate, strada, numar))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel MAGAZIN", fg="brown", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Id magazin:").place(x=30, y=100)
        Label(root, text="Nume:").place(x=30, y=140)
        Label(root, text="Localitate:").place(x=30, y=180)
        Label(root, text="Strada:").place(x=30, y=220)
        Label(root, text="Numar:").place(x=30, y=260)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        e4 = Entry(root)
        e4.place(x=170, y=220)

        e5 = Entry(root)
        e5.place(x=170, y=260)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort id_magazin", command=sortid, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort nume", command=sortnum, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort localitate", command=sortloc, height=3, width=13).place(x=650, y=240)
        Button(root, text="Sort numar", command=sortnr, height=3, width=13).place(x=800, y=100)

        cols = ('id_magazin', 'nume', 'localitate', 'strada', 'numar')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)

        show()
        listBox.bind('<Double-Button-1>', GetValue)

    elif cmb.get() == "Transport":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)

            e1.insert(0, select['nr_masina'])
            e2.insert(0, select['firma_curierat'])
            e3.insert(0, select['id_sofer'])

        def Add():
            transnr = e1.get()
            transfir = e2.get()
            transid = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  transport (nr_masina, firma_curierat, id_sofer) VALUES (%s, %s, %s)"
                val = (transnr, transfir, transid)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Transport inserted successfully")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            transnr = e1.get()
            transfir = e2.get()
            transid = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  transport set firma_curierat= %s,id_sofer= %s where nr_masina= %s"  % (
                update = "Update  transport set firma_curierat= '%s',id_sofer= '%s' where nr_masina= '%s'" % (
                    transfir, transid, transnr)
                # val = (transnr, transfir, transid)
                mycursor.execute(update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            transnr = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from transport where nr_masina= %s"
                val = (transnr,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def sortnr():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM transport ORDER BY nr_masina")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_masina, firma_curierat, id_sofer) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_masina, firma_curierat, id_sofer))
                mysqldb.close()

        def sortfirm():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM transport ORDER BY firma_curierat")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_masina, firma_curierat, id_sofer) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_masina, firma_curierat, id_sofer))
                mysqldb.close()

        def sortidsof():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")

            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT * FROM transport ORDER BY id_sofer")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_masina, firma_curierat, id_sofer) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_masina, firma_curierat, id_sofer))
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="bananaverde.ro20",
                                              database="depozit")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT nr_masina, firma_curierat, id_sofer FROM transport")
            records = mycursor.fetchall()
            print(records)

            for i, (nr_masina, firma_curierat, id_sofer) in enumerate(records, start=1):
                listBox.insert("", "end", values=(nr_masina, firma_curierat, id_sofer))
                mysqldb.close()

        root = Tk()
        root.geometry("1200x600")

        tk.Label(root, text="Tabel TRANSPORT", fg="purple", font=("Times New Roman", 20)).place(x=150, y=10)

        tk.Label(root, text="Numar masina:").place(x=30, y=100)
        Label(root, text="Firma curierat:").place(x=30, y=140)
        Label(root, text="Id sofer:").place(x=30, y=180)

        e1 = Entry(root)
        e1.place(x=170, y=100)

        e2 = Entry(root)
        e2.place(x=170, y=140)

        e3 = Entry(root)
        e3.place(x=170, y=180)

        Button(root, text="Add", command=Add, fg="blue", height=3, width=13).place(x=400, y=100)
        Button(root, text="Update", command=update, fg="purple", height=3, width=13).place(x=400, y=170)
        Button(root, text="Delete", command=delete, fg="red", height=3, width=13).place(x=400, y=240)
        Button(root, text="Sort nr_masina", command=sortnr, height=3, width=13).place(x=650, y=100)
        Button(root, text="Sort firma", command=sortfirm, height=3, width=13).place(x=650, y=170)
        Button(root, text="Sort id_sofer", command=sortidsof, height=3, width=13).place(x=650, y=240)

        cols = ('nr_masina', 'firma_curierat', 'id_sofer')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=350)


        show()

        listBox.bind('<Double-Button-1>', GetValue)



btn = ttk.Button(root, text="Get Table", command=opt)
btn.place(relx="0.5", rely="0.1")
btn.grid(column=0, row=2, padx=10, pady=2)
root.mainloop()


