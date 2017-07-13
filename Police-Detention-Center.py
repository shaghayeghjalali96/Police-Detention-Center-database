import psycopg2
conn = psycopg2.connect(database="office", user="postgres", password="12345678",host='127.0.0.1')
cur = conn.cursor()
num='1'
while (num=='1'):
  print("enter cr =>creat table")
  print("enter in =>insert table")
  print("enter up =>update table")
  print("enter sh=>show inform")
  print("enter else=>else")
  var = input('enter char :')
  if var == 'cr':
     print ("cr - Got a true expression value creat table") 
     print ("enter em for CREATE edari_man TABLE  ")
     print ("enter jorm for CREATE jorm TABLE  ")
     print ("enter pman for CREATE police-man TABLE  ")
     print ("enter baz for CREATE BAZDASHT TABLE  ")
     print ("enter zendan for CREATE zendan TABLE  ")
     print ("enter mojrem for CREATE mojrem TABLE  ") 
     print ("enter sakht for CREATE sakhteman TABLE  ") 
     print ("enter edari for CREATE sakhteman_edari TABLE  ")
     print ("enter karkonan for CREATE karkonan TABLE  ")
     print ("enter mahal for CREATE EDARI_MAHAL TABLE  ")
     print ("enter habs for CREATE habs TABLE  ")
     com =input ('enter char to creat table  :')
     if com =='em':
       cur.execute('''CREATE TABLE edari_man
          (id_em INT PRIMARY KEY     NOT NULL,        
           name           TEXT    NOT NULL,
           age            INT     NOT NULL,
           jensiat        CHAR(20),
           salary         REAL,
           sale_estekhdam int,
           takhasos       text);''')
       print ("Table created successfully")
       conn.commit()
     elif com=='jorm':
       cur.execute('''CREATE TABLE jorm
          (id_jo INT PRIMARY KEY     NOT NULL,
           name           TEXT    NOT NULL,
           daste          TEXT);''')
       print ("Table created successfully")
       conn.commit()
     elif com=='baz':  
        cur.execute('''CREATE TABLE bazdasht
        (
             id_mj integer NOT NULL,
             id_po integer,
             id_jo integer,
             date_bazdasht   date,
             date_anjamjorm   date,
             CONSTRAINT "bazdasht_pkey" PRIMARY KEY (id_mj,date_bazdasht),
             CONSTRAINT "bazdasht_id_mj_fkey" FOREIGN KEY (id_mj)
             REFERENCES mojrem (id_mj) MATCH SIMPLE
             ON UPDATE NO ACTION ON DELETE NO ACTION );''')
        print ("Table created successfully")
        conn.commit()
     elif com=='habs': 
       cur.execute('''CREATE TABLE habs
       (
           shoro_habs date,
           id_mj integer NOT NULL,
           id_ze integer,
           payan_habs date,
           CONSTRAINT habs_pkey PRIMARY KEY (id_mj,shoro_habs),
           CONSTRAINT "habs_id_mj_fkey" FOREIGN KEY (id_mj)
           REFERENCES mojrem (id_mj) MATCH SIMPLE
           ON UPDATE NO ACTION ON DELETE NO ACTION);''')
       conn.commit()
     elif com=='pman':
        cur.execute('''CREATE TABLE police_man
        (
             id_po INT PRIMARY KEY     NOT NULL,
             name           TEXT    NOT NULL,
             age            INT     NOT NULL,
             jensiat        CHAR(20),
             salary         REAL,
             sale_estekhdam int,
             takhasos       text);''')
        print ("Table created successfully")
        conn.commit()
     elif com=='zendan':
        cur.execute('''CREATE TABLE zendan
        (
             id_ze INT PRIMARY KEY     NOT NULL,
             name           TEXT    NOT NULL,
             zarfiat        INT     NOT NULL,
             jensiat        CHAR(20),
             makan          text);''')
        print ("Table created successfully")
        conn.commit()
     elif com=='mojrem':
        cur.execute('''CREATE TABLE mojrem
        (
             id_mj INT PRIMARY KEY     NOT NULL,
             name           TEXT    NOT NULL,
             age            INT     NOT NULL,
             jensiat        CHAR(50));''')
        print ("Table created successfully")
        conn.commit()
     elif com=='sakht':
        cur.execute('''CREATE TABLE sakhteman
        (
             id INT PRIMARY KEY     NOT NULL,
             name           TEXT    NOT NULL);''')
        print ("Table created successfully")
        conn.commit()
     elif com=='edari':        
        cur.execute('''CREATE TABLE sakhteman_edari
        (
             id_se INT PRIMARY KEY     NOT NULL,
             name_se           TEXT     NOT NULL,
             addres         TEXT     NOT NULL);''')
        print ("Table created successfully")
        conn.commit()
     elif com=='karkonan':
        cur.execute('''CREATE TABLE karkonan
        (
             id INT PRIMARY KEY     NOT NULL,
             name           TEXT    NOT NULL);''')
        print ("Table created successfully")
        conn.commit()
     elif com=='mahal':
        cur.execute('''CREATE TABLE edari_mahal
        (
           id_em integer NOT NULL,
           id_se integer NOT NULL,
           CONSTRAINT edari_mahal_pkey PRIMARY KEY (id_em,id_se),
           CONSTRAINT edari_mahal_id_em_fkey FOREIGN KEY (id_em)
           REFERENCES edari_man (id_em) MATCH SIMPLE
           ON UPDATE NO ACTION ON DELETE NO ACTION,
           CONSTRAINT edari_mahal_id_se_fkey FOREIGN KEY (id_se)
           REFERENCES sakhteman_edari (id_se) MATCH SIMPLE
           ON UPDATE NO ACTION ON DELETE NO ACTION); ''')
        print ("Table created successfully")
        conn.commit()
  elif var =='in':
      print ("in - Got a true expression value insert")
      print ("in - Got a true expression value insert")
      print ("enter eman for INSERT edari_man TABLE  ")
      print ("enter jorm for INSERT jorm TABLE  ")
      print ("enter pman for INSERT police-man TABLE  ")
      print ("enter bazdasht for INSERT BAZDASHT TABLE  ")
      print ("enter zendan for INSERT zendan TABLE  ")
      print ("enter mojrem for INSERT mojrem TABLE  ") 
      print ("enter sakhteman for INSERT sakhteman TABLE  ") 
      print ("enter sakhtemanedari for INSERT sakhteman_edari TABLE  ")
      print ("enter kar for INSERT karkonan TABLE  ")
      print ("enter edarimahal for INSERT EDARI_MAHAL TABLE  ")
      print ("enter habs for INSERT habs TABLE  ")
      com =input ('enter char to insert table  :')
      if com == 'kar' :
         a=input('enter name:')
         s=input('enter id:')
         cur.execute("INSERT INTO karkonan (id,name ) \
              VALUES (%s, %s )",(s,a,));
         conn.commit()
         print ("Records created successfully");
      elif com=='zendan':
         s=input('enter id:')
         a=input('enter name:')
         z=input('enter zarfiat:')
         c=input('enter jensiat:')
         e=input('enter makan:')
         cur.execute("INSERT INTO zendan (id_ze,name,zarfiat,jensiat, makan) \
             VALUES (%s, %s,%s, %s,%s)",(s,a,z,c,e));
         conn.commit()
         print ("Records created successfully")
      elif com == 'eman' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter name_em:')
         s=input('enter id :')
         d=input('enter age :')
         w=input('enter jensiat:')
         r=input('enter SALARY:')       
         t=input('enter sale_estekhdam:')       
         y=input('enter takhasos:')        
         cur.execute("INSERT INTO edari_man (id_em,name,age,jensiat,salary,sale_estekhdam,takhasos ) \
             VALUES (%s, %s, %s, %s, %s, %s, %s )",(s,a,d,w,r,t,y));
         conn.commit()
         print ("Records created successfully")
      elif com == 'jorm' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter name:')
         s=input('enter id :')   
         w=input('enter daste :')    
         cur.execute("INSERT INTO jorm (id_jo,name,daste ) \
             VALUES (%s, %s )",(s,a,w));
         conn.commit()
         print ("Records created successfully")
      elif com == 'bazdasht' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter id_mj:')
         s=input('enter id_po:')
         d=input('enter id_jo:')
         w=input('enter date_bazdasht:')
         r=input('enter date_anjamjorm:')             
         cur.execute("INSERT INTO BAZDASHT (id_mj,id_po,id_jo,date_bazdasht,date_anjamjorm ) \
             VALUES (%s, %s, %s, %s, %s )",(a,s,d,w,r));
         conn.commit()
         print ("Records created successfully")
      elif com == 'pman' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter name:')
         s=input('enter id_po:')
         d=input('enter age :')
         w=input('enter jensiat:')
         r=input('enter salary:')       
         t=input('enter sale_estekhdam:')       
         y=input('enter takhasos:')        
         cur.execute("INSERT INTO police_man (id_po,name,age,jensiat,salary,sale_estekhdam,takhasos ) \
             VALUES (%s, %s, %s, %s, %s, %s, %s )",(s,a,d,w,r,t,y));
         conn.commit()
         print ("Records created successfully")
      elif com == 'mojrem' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter name:')
         s=input('enter id_mj :')
         d=input('enter age :')
         w=input('enter jensiat:')       
         cur.execute("INSERT INTO mojrem (id_mj,name,age,jensiat ) \
             VALUES (%s, %s , %s, %s)",(s,a,d,w))
         conn.commit()
         print ("Records created successfully")
      elif com == 'sakhteman' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter name:')
         s=input('enter id :')       
         cur.execute("INSERT INTO sakhteman (Id,name ) \
             VALUES (%s, %s )",(s,a));
         conn.commit()
         print ("Records created successfully")
      elif com == 'sakhtemanedari' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter id_se:')
         s=input('enter name_se :')
         d=input('enter addres:')       
         cur.execute("INSERT INTO sakhteman_edari (id_se, name_se,addres ) \
             VALUES (%s, %s, %s )",(s,a.d));
         conn.commit()
         print ("Records created successfully")
      elif com == 'edarimahal' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter id_em:')
         s=input('enter id_se :')      
         cur.execute("INSERT INTO edari_mahal (id_em,id_se ) \
             VALUES (%s, %s )",(s,a));
         conn.commit()
         print ("Records created successfully")
      elif com == 'habs' :
         print ("Opened database successfully")
         cur = conn.cursor()
         a=input('enter shoro_habs:')
         s=input('enter  id_mj:')
         d=input('enter id_ze:')
         w=input('enter payan_habs:')             
         cur.execute('''INSERT INTO habs (shoro_habs,id_mj,id_ze,payan_habs ) \
             VALUES (%s, %s, %s, %s)''',(a,s,d,w));
         conn.commit()
         print ("Records created successfully");
  elif var == 'up':
     print ("in - Got a true expression value insert")
     print ("enter eman for INSERT edari_man TABLE  ") 
     print ("enter jorm for INSERT jorm TABLE  ")  
     print ("enter pman for INSERT police-man TABLE  ") 
     print ("enter bazdasht for INSERT BAZDASHT TABLE  ")
     print ("enter ze for INSERT zendan TABLE  ") 
     print ("enter mojrem for INSERT mojrem TABLE  ")
     print ("enter sakhteman for INSERT sakhteman TABLE  ") 
     print ("enter sakhtemanedari for INSERT sakhteman_edari TABLE  ") 
     print ("enter karkonan for INSERT karkonan TABLE  ")  
     print ("enter edarimahal for INSERT edari_mahal TABLE  ") 
     print ("enter habs for INSERT habs TABLE  ") 
     com =input ('enter char to insert table  :')	
     if com =='edari':
         a=input('enter id_se you want to update information about it:')
         s=input('enter name_se :')
         d=input('enter addres:') 
         cur.execute('''update sakhteman_edari set  name_se=%s where id_se=%s ''',(s,a))
         cur.execute('''update sakhteman_edari set  addres=%s where id_se=%s ''',(d,a))
         print ("Table updated successfully")
         conn.commit()
     elif com =='eman': 
          s=input('enter id_em you want to update information about it:')
          a=input('enter name:')
          d=input('enter age :')
          w=input('enter jensiat:')
          r=input('enter salary:')       
          t=input('enter sale_estekhdam:')       
          y=input('enter takhasos:') 
          cur.execute('''update edari_man set name=%s where id_me=%s''',(a,s))
          cur.execute('''update edari_man set age=%s where id_me=%s''',(d,s))
          cur.execute('''update edari_man set jensiat=%s where id_me=%s''',(w,s))
          cur.execute('''update edari_man set salary=%s where id_me=%s''',(r,s))
          cur.execute('''update edari_man set sale_estekhdam=%s where id_me=%s''',(t,s))
          cur.execute('''update edari_man set takhasos=%s where id_me=%s''',(y,s))
          print ("Table updated successfully")
          conn.commit() 
     elif com=='ze':
         s=input('enter id_ze  you want to update information about it :')
         a=input('enter name:')
         z=input('enter zarfiat:')
         c=input('enter jensiat:')
         e=input('enter makan:')
         cur.execute('''update zendan set name=%s where id_ze=%s''',(a,s))
         cur.execute('''update zendan set jensiat=%s where id_ze=%s''',(c,s))
         cur.execute('''update zendan set zarfiat=%s where id_ze=%s''',(z,s))
         cur.execute('''update zendan set makan=%s where id_ze=%s''',(e,s))
         print ("Table updated successfully")
         conn.commit()
     elif com == 'jorm' :
         s=input('enter id_jo  you want to update information about it:') 
         a=input('enter name:')  
         w=input('enter daste :') 
         cur.execute('''update jorm set name=%s where id_jo=%s''',(a,s))
         cur.execute('''update jorm set daste=%s where id_jo=%s''',(w,s))   
         print ("Table updated successfully")
         conn.commit()
     elif com == 'pman' :
         s=input('enter id_po you want to update information about it:')
         a=input('enter name:')
         d=input('enter age :')
         w=input('enter jensiat:')
         r=input('enter salary:')       
         t=input('enter sale_estekhdam:')       
         y=input('enter takhasos:')
         cur.execute('''update police_man set name=%s where id_po=%s''',(a,s))
         cur.execute('''update police_man set age=%s where id_po=%s''',(d,s))
         cur.execute('''update police_man set jensiat=%s where id_po=%s''',(w,s))
         cur.execute('''update police_man set salary=%s where id_po=%s''',(r,s))
         cur.execute('''update police_man set sale_estekhdam=%s where id_po=%s''',(t,s))
         cur.execute('''update police_man set takhasos=%s where id_po=%s''',(y,s)) 
         print ("Table updated successfully")
         conn.commit() 
     elif com == 'bazdasht' :
         a=input('enter id_mj you want to update information about it:')
         s=input('enter id_po:')
         d=input('enter id_jo:')
         w=input('enter date_bazdasht:')
         r=input('enter date_anjamjorm:')
         cur.execute('''update bazdasht set id_po=%s where id_mj=%s''',(s,a))
         cur.execute('''update bazdasht set id_jo=%s where id_mj=%s''',(d,a))
         cur.execute('''update bazdasht set date_bazdasht=%s where id_mj=%s''',(w,a))
         cur.execute('''update bazdasht set date_anjamjorm=%s where id_mj=%s''',(r,a))
         print ("Table updated successfully")
         conn.commit()
     elif com == 'habs' :
         s=input('enter id_mj you want to update information about it:')
         a=input('enter shoro_habs:')
         d=input('enter id_ze:')
         w=input('enter payan_habs:')
         cur.execute('''update habs set id_ze=%s where id_mj=%s''',(d,s))
         cur.execute('''update habs set shoro_habs=%s where id_mj=%s''',(a,s))
         cur.execute('''update habs set payan_habs=%s where id_mj=%s''',(w,s))        
         print ("Table updated successfully")
         conn.commit()
     elif com == 'mojrem' :
         s=input('enter id_mj want to update information about it :')
         a=input('enter name:')
         d=input('enter age :')
         w=input('enter jensiat:') 
         cur.execute('''update mojrem set name=%s where id_mj=%s''',(a,s))
         cur.execute('''update mojrem set age=%s where id_mj=%s''',(d,s))
         cur.execute('''update mojrem set jensiat=%s where id_mj=%s''',(w,s))        
         print ("Table updated successfully")
         conn.commit()
     elif com == 'edarimahal' :
         s=input('enter id_se  want to update information about it:')
         a=input('enter id_em:')      
         cur.execute('''update edari_mahal set id_em=%s where id_se=%s''',(a,s))    
         print ("Table updated successfully")
         conn.commit()
     elif com == 'karkonan' :
         s=input('enter id want to update information about it:')
         a=input('enter name:')
         cur.execute('''update karkonan set name=%s where id=%s''',(a,s))    
         print ("Table updated successfully")
         conn.commit()
     elif com == 'sakhteman' :
         s=input('enter id want to update information about it:')
         a=input('enter name:')
         cur.execute('''update sakhteman set name=%s where id=%s''',(a,s))
         print ("Table updated successfully")
         conn.commit()
  elif var=='sh':  
      print ("enter 1 show police man inform*")  
      print ("enter 2 show mojrem inform*")
      print ("enter 3 show zendan inform*") 
      print ("enter 4 show edari man inform*")
      print ("enter 5 show sakhteman edari inform*")
      print ("enter 6 show jorm inform*")
      var1=input("enter")
      if var1 == '1':
         print ("1 - Got a true expression value find *")
         def show1 (): 
            a=input('inter id police')
            cur.execute('''SELECT * FROM police_man where id_po = %s''', (a,))
            print( cur.fetchall())
            conn.commit()
         show1()   
      elif var1 == '2':
         print ("2 - Got a true expression value find *")
         def show2 (): 
            a=input('inter id mojrem')
            cur.execute('''SELECT * FROM mojrem where id_mj = %s''', (a,))
            print( cur.fetchall())
            conn.commit()
         show2() 
      elif var1 =='3':
          print ("3 - Got a true expression value find *")
          def show3 (): 
              a=input('inter id zendan')
              cur.execute('''SELECT * FROM zendan where id_ze = %s''', (a,))
              print( cur.fetchall())
              conn.commit()
          show3() 
      elif var1 =='4':
          print ("4 - Got a true expression value find *")
          def show4 (): 
              a=input('inter id edariman')
              cur.execute('''SELECT * FROM edari_man where id_em = %s''', (a,))
              print( cur.fetchall())
              conn.commit()
          show4() 
      elif var1 =='5':
          print ("5 - Got a true expression value find *")
          def show5 (): 
              a=input('inter id sakhteman edari')
              cur.execute('''SELECT * FROM sakhteman_edari where id_se = %s''', (a,))
              print( cur.fetchall())
              conn.commit()
          show5() 
      elif var1 =='6':
          print ("6 - Got a true expression value find *")
          def show6 (): 
              a=input('inter id sakhteman edari')
              cur.execute('''SELECT * FROM jorm where id_jo = %s''', (a,))
              print( cur.fetchall())
              conn.commit()
          show6()
      else:
	      print("Got a false expression value")
  elif var=='else':   
    print ("enter 1  modat zaman mabin ertekab har jorm va bazdasht shodan tavasot police on mojrem*") 
    print ("enter 2 mojrem hai ke yek police grefte*")
    print ("enter 3 sabegh yek mojrem*")
    print ("enter 4 tedad zendani haie yek zendan*")
    print ("enter 5 tedad afrad habs shode moanas*")
    print ("enter 6 tedad karmandan moanas*")
    print ("enter 7 miangin sen zendanian yek zendan*")
    print ("enter 8 name afrad zire 25 sal*")
    print ("enter 9 ke sale bad mitavanand bazneshast shavand*")
    print ("enter 10 max jorm afrad zir 25 sal*")
    print ("enter 11 zaman anjam yek jorm*")
    print ("enter 12 karmandani ke ghabl az 1995 estekhdam shodan*")
    print ("enter 13 mojreman yek zendan moshakhas*")
    print ("enter 14 zendan haee ke zarfiat bala 1000 va moanas hastand*")
    print ("enter 15 mojremani ke jorm  moshtarak darand*")
    print ("enter 16 karmandani ke dar bakhsh edari semat moshtarak darand*")
    print ("enter 17 karmandani ke dar yek sakhteman moshakhas hastan*")
    print ("enter 18 police ke mojremi nagrefte*")
    print ("enter 19 shologh tarin zendanha*")
    print ("enter 20 mojreman zani ke 2 jorm motafavet darand*")
    print ("enter 21 bishtarin jorm tekrar shode*")
    print ("enter 22 zendani ke kamtar az dah nafar zarfiat dare*")
    print ("enter 23 zendani ke bishtar az nesfe an khalie*")
    print ("enter 24 mojremi ke bazdasht shode ama habs nashode*")
    print ("enter 25 sabeghe dar tarin*")
    print ("enter 26 mojremani ke bishtar az 2 sal mahkom be habs shode and*")
    print ("enter 27 zanani ke dar sal 1393 ghatl anjam dade and*")
    print ("enter 28 bishtarin ghatl dar che mahi sorat gerefte *")
    print ("enter 29 bishtarin jormi ke dar har mah anjam gerefte *")  
    print ("enter 30 sabeghe darhai moanas*")
    var1=input("enter") 
    if var1 == '2':
        def f1 ():
            a=input('enter id police')
            cur.execute('''SELECT mojrem.name FROM police_man natural join bazdasht join  mojrem on mojrem.id_mj=bazdasht.id_mj where id_po = %s''', (a,))
            for a in cur.fetchall():
	            print(a)
            conn.commit() 
        f1 ()
    elif var1 =='3':
        print ("3 - Got a true expression value find *")
        def f2():
            a=input('enter id mojrem')
            cur.execute('''SELECT jorm.name FROM bazdasht join  jorm on jorm.id_jo=bazdasht.id_jo where id_mj = %s''', (a,))
            for a in cur.fetchall():
	            print(a)
            conn.commit()
        f2()    
    elif var1 =='4':
        print ("4 - Got a true expression value find *")
        def f3():
            a=input('enter id zendan')
            cur.execute('''SELECT count(*) FROM habs where id_ze = %s ''', (a,))
            n=cur.fetchone()
            print(n)
            conn.commit()
        f3()    
    elif var1 =='5':
        print ("5 - Got a true expression value find *")
        def f4():
            cur.execute('''SELECT count(*) FROM habs join mojrem on habs.id_mj=mojrem.id_mj where jensiat = 'moanas' ''')
            print( cur.fetchall())
            conn.commit()
        f4()    
    elif var1 =='6':
        print ("6 - Got a true expression value find *")
        def f5():
            cur.execute('''SELECT count(*) FROM edari_man where jensiat = 'moanas' ''')
            print( cur.fetchall())
            conn.commit()
        f5()
    elif var1 =='7':
        print ("7 - Got a true expression value find *")
        def f6():
            a=input('enter id zendan')
            cur.execute('''SELECT avg(age) FROM habs join mojrem on habs.id_mj=mojrem.id_mj where id_ze = %s ''', (a,))
            print(cur.fetchone())
            conn.commit()
        f6()
    elif var1 =='8':
        print ("8 - Got a true expression value find *")
        def f7():
            cur.execute('''SELECT name FROM mojrem where age<25 ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f7()
    elif var1 =='9':
        print ("9 - Got a true expression value find *")
        def f8():
            cur.execute(''' SELECT name_em from edari_man where sale_estekhdam<1987''')
            print(cur.fetchone())
            conn.commit()
        f8()
    elif var1 =='10':
        print ("10 - Got a true expression value find *")
        def f9():
            cur.execute('''SELECT jorm.name,count(*) maximum FROM bazdasht join mojrem on bazdasht.id_mj=mojrem.id_mj join jorm on bazdasht.id_jo=jorm.id_jo
            where age<25 group by jorm.id_jo  ORDER BY maximum DESC ''')
            print(cur.fetchone())
            conn.commit()
        f9()
    elif var1 =='11':
        print ("11 - Got a true expression value find *")
        def f10():
            a=input('enter id jorm')
            cur.execute('''SELECT date_anjamjorm FROM bazdasht where id_jo = %s ''', (a,))
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f10()
    elif var1 =='12':
        print ("12 - Got a true expression value find *")
        def f11():
            cur.execute('''SELECT name_em from edari_man where sale_estekhdam<1995''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f11()    
    elif var1 == '13':
        print ("13 - Got a true expression value find *")
        def f12():
            a=input('enter id zendan')
            cur.execute('''SELECT name FROM habs join mojrem on habs.id_mj = mojrem.id_mj where id_ze = %s''',(a,) )
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f12()   
    elif var1 == '14':
        print ("14 - Got a true expression value find *")
        def f13():
            cur.execute('''SELECT name FROM zendan where zarfiat > 1000 and jensiat = 'moanas' ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f13()
    elif var1 == '15': 
        print ("15 - Got a true expression value find *")
        def f14():
            cur.execute('''SELECT mojrem.name as mname,jorm.name as jname FROM mojrem join bazdasht on bazdasht.id_mj = mojrem.id_mj join jorm on jorm.id_jo = bazdasht.id_jo order by bazdasht.id_jo  ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f14()
    elif var1 == '16': 
        print ("16 - Got a true expression value find *")
        def f16():
            cur.execute('''SELECT name_em,takhasos FROM edari_man order by takhasos  ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f16()
    elif var1=='17':
        print ("17 - Got a true expression value find *")
        def f17():
            a=input('enter id sakhteman edari')
            cur.execute('''SELECT edari_man.name_em FROM sakhteman_edari natural join mahal natural join edari_man where id_se = %s''',(a,) )
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f17()
    elif var1=='18':
        print ("18 - Got a true expression value find *")
        def f18():
            cur.execute('''select name from police_man where id_po in (SELECT id_po from police_man except select id_po from bazdasht)''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f18()
    elif var1=='19':
        print ("19 - Got a true expression value find *")
        def f19():
            cur.execute('''SELECT name,count(*) maximum FROM habs join zendan on zendan.id_ze=habs.id_ze 
              group by zendan.id_ze  ORDER BY maximum DESC ''')
            print( cur.fetchone())
            conn.commit()
        f19()    
    elif var1=='20': 
        print ("20 - Got a true expression value find *")
        def f20():
            cur.execute('''SELECT name ,count(id_jo) FROM mojrem join bazdasht on mojrem.id_mj=bazdasht.id_mj where jensiat='moanas' group by bazdasht.id_mj,name having count(id_jo) = 2  ''' )
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f20()    
    elif var1=='21':
        print ("21 - Got a true expression value find *")
        def f21():
            cur.execute('''SELECT name ,count(jorm.id_jo) FROM jorm join bazdasht on jorm.id_jo=bazdasht.id_jo group by bazdasht.id_jo,name ORDER BY count(jorm.id_jo) desc  ''' )
            for a in cur.fetchone():
                print(a)
            conn.commit()
        f21()
    elif var1 =='22':
        print ("22 - Got a true expression value find *")
        def f22():
            cur.execute('''SELECT count(*),zarfiat,name FROM zendan full outer join habs on zendan.id_ze=habs.id_ze group by zendan.id_ze ''' )
            for a in cur.fetchall():
                for l1 in a:
                    s=a[1]
                    c=a[0]
                    d=s-c
                if d<10:
                     print(a[2])
                print()
            conn.commit()
        f22()
    elif var1 =='23':
        print ("23 - Got a true expression value find *")
        def f23():
            cur.execute('''SELECT count(*),zarfiat,name FROM zendan full outer join habs on zendan.id_ze=habs.id_ze group by zendan.id_ze ''' )
            for a in cur.fetchall():
                for l1 in a:
                    s=a[1]
                    c=a[0]
                print()
                d=s/c
                if d>.5:
                    print(a[2])
            conn.commit()
        f23()
    elif var1=='24':
        print ("24 - Got a true expression value find *")
        def f24():
            cur.execute('''select name from mojrem where id_mj in (SELECT id_mj from bazdasht except select id_mj from habs)''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f24()
    elif var1=='25': 
        print ("25 - Got a true expression value find *")
        def f25():
            cur.execute('''SELECT name,count(*) FROM mojrem join bazdasht on mojrem.id_mj=bazdasht.id_mj group by mojrem.id_mj ORDER BY count(*) desc  ''' )
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f25()
    elif var1=='26':
        print ("26 - Got a true expression value find *")
        def f26():
            cur.execute('''SELECT name FROM mojrem join habs on mojrem.id_mj=habs.id_mj where (extract(year from payan_habs ))- (extract(year from shoro_habs )) > 0002  ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f26()
    elif var1=='27':
        print ("27 - Got a true expression value find *")
        def f27():
            cur.execute('''SELECT mojrem.name FROM mojrem join bazdasht on mojrem.id_mj=bazdasht.id_mj join jorm on bazdasht.id_jo=jorm.id_jo where (extract(year from date_anjamjorm )) =1993 and jorm.name='ghatl' and jensiat='zan'  ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f27()
    elif var1=='28':
        print ("28 - Got a true expression value find *")
        def f28():
            cur.execute('''SELECT extract(month from date_anjamjorm ) FROM  bazdasht join jorm on bazdasht.id_jo=jorm.id_jo where jorm.name='ghatl' group by extract(month from date_anjamjorm ) order by count(extract(month from date_anjamjorm )) desc   ''')
            for a in cur.fetchone():
                print(a)
            conn.commit()
        f28()
    elif var1=='29':
        print ("29 - Got a true expression value find *")
        def f29():
            cur.execute('''SELECT name,(extract(month from date_anjamjorm )) FROM  bazdasht join jorm on bazdasht.id_jo=jorm.id_jo group by jorm.name,extract(month from date_anjamjorm ) order by count(extract(month from date_anjamjorm )) desc   ''')
            for a in cur.fetchall():
                print(a)
            conn.commit()
        f29()   
    elif var1 =='30':
        print ("30 - Got a true expression value find *")
        def f30():
            cur.execute('''SELECT name,count(*) FROM mojrem join bazdasht on mojrem.id_mj=bazdasht.id_mj where jensiat='moanas' group by mojrem.id_mj ORDER BY count(*) desc ''')
            for a in cur.fetchall():
	            print(a)
            conn.commit()
        f30()      
    elif var1 =='1': 
        print ("33 - Got a true expression value find *")
        def f33():
            cur.execute('''SELECT mojrem.name,jorm.name, (date_bazdasht-date_anjamjorm) FROM  bazdasht join jorm on bazdasht.id_jo=jorm.id_jo join mojrem on mojrem.id_mj=bazdasht.id_mj  group by mojrem.name,jorm.name,(date_bazdasht-date_anjamjorm)  ''') 
            for a in cur.fetchall():
	            print(a)
            conn.commit()
        f33()
    else:
	    print("Got a false expression value")                                              
  else:
      print ("Got a false expression value")
  print("enter if you have another work and 0 for exit")
  num=input()
print ("Good bye!")
conn.close()
