import tkinter
import tkinter.scrolledtext as tkst
import sqlite3

def main_win():
    main_window = tkinter.Tk()
    main_window.title('D&D Helping Tool')
    main_window.geometry("500x500")
    main_window.resizable(0, 0)

    button1 = tkinter.Button(main_window, text="Add monster", command=add_monster_win)
    button1.pack()

    button2 = tkinter.Button(main_window, text="Add NPC", command=add_npc_win)
    button2.pack()

    button3 = tkinter.Button(main_window, text="Generate Fight", command=generate_fight_window)
    button3.pack()

    main_window.mainloop()

def add_npc_win():
    #declare all f*cking variables as global.........
    global add_npc_window
    global w2_txt1
    global w2_txt2_input
    global w2_txt3
    global w2_txt4_input
    global w2_txt5
    global w2_txt6_input
    global w2_txt7
    global w2_txt8_input
    global w2_txt9
    global w2_txt10_input
    global w2_txt11
    global w2_txt12_input
    global w2_txt13
    global w2_txt14_input
    global w2_txt15
    global w2_txt16_input
    global w2_txt17
    global w2_txt18_input
    global w2_txt19
    global w2_txt20_input
    global w2_txt21
    global w2_txt22_input
    global w2_txt23
    global w2_txt24_input
    global homebrew_txt
    global homebrew_listbox
    global ch_rating_txt
    global ch_rating_scale
    global add_monster_btn
    global add_monster_creature_type_txt
    global add_monster_creature_type

    #window stats
    add_npc_window = tkinter.Tk()
    add_npc_window.title("Add NPC")
    add_npc_window.geometry("800x800")
    add_npc_window.resizable(1, 1)

    #add monster stats
    w2_txt1 = tkinter.Label(add_npc_window, text="Name:")
    w2_txt1.grid(row=1, column=1)
    w2_txt2_input = tkinter.Entry(add_npc_window)
    w2_txt2_input.grid(row=1, column=2, sticky=tkinter.W)

    w2_txt3 = tkinter.Label(add_npc_window, text="Armor Class:")
    w2_txt3.grid(row=2, column=1)
    w2_txt4_input = tkinter.Entry(add_npc_window)
    w2_txt4_input.grid(row=2, column=2, sticky=tkinter.W)

    w2_txt5 = tkinter.Label(add_npc_window, text="Hit Points:")
    w2_txt5.grid(row=3, column=1)
    w2_txt6_input = tkinter.Entry(add_npc_window)
    w2_txt6_input.grid(row=3, column=2, sticky=tkinter.W)

    w2_txt7 = tkinter.Label(add_npc_window, text="Speed:")
    w2_txt7.grid(row=4, column=1)
    w2_txt8_input = tkinter.Entry(add_npc_window)
    w2_txt8_input.grid(row=4, column=2, sticky=tkinter.W)

    w2_txt9 = tkinter.Label(add_npc_window, text="STR:")
    w2_txt9.grid(row=5, column=1)
    w2_txt10_input = tkinter.Entry(add_npc_window)
    w2_txt10_input.grid(row=5, column=2, sticky=tkinter.W)

    w2_txt11 = tkinter.Label(add_npc_window, text="DEX:")
    w2_txt11.grid(row=6, column=1)
    w2_txt12_input = tkinter.Entry(add_npc_window)
    w2_txt12_input.grid(row=6, column=2, sticky=tkinter.W)

    w2_txt13 = tkinter.Label(add_npc_window, text="CON:")
    w2_txt13.grid(row=7, column=1)
    w2_txt14_input = tkinter.Entry(add_npc_window)
    w2_txt14_input.grid(row=7, column=2, sticky=tkinter.W)

    w2_txt15 = tkinter.Label(add_npc_window, text="INT:")
    w2_txt15.grid(row=8, column=1)
    w2_txt16_input = tkinter.Entry(add_npc_window)
    w2_txt16_input.grid(row=8, column=2, sticky=tkinter.W)

    w2_txt17 = tkinter.Label(add_npc_window, text="WIS:")
    w2_txt17.grid(row=9, column=1)
    w2_txt18_input = tkinter.Entry(add_npc_window)
    w2_txt18_input.grid(row=9, column=2, sticky=tkinter.W)

    w2_txt19 = tkinter.Label(add_npc_window, text="CHA:")
    w2_txt19.grid(row=10, column=1)
    w2_txt20_input = tkinter.Entry(add_npc_window)
    w2_txt20_input.grid(row=10, column=2, sticky=tkinter.W)

    #this is the two long text box
    w2_txt21 = tkinter.Label(add_npc_window, text="Skills:")
    w2_txt21.grid(row=11, column=1, sticky=tkinter.W)
    w2_txt22_input = tkinter.Text(add_npc_window, height=10, width=50)
    w2_txt22_input.grid(row=11, column=2, sticky=tkinter.W)

    w2_txt23 = tkinter.Label(add_npc_window, text="Actions:")
    w2_txt23.grid(row=12, column=1, sticky=tkinter.W)
    w2_txt24_input = tkinter.Text(add_npc_window, height=10, width=50)
    w2_txt24_input.grid(row=12, column=2, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=13)

    #listbox : homebrew or book

    homebrew_listbox = tkinter.Listbox(add_npc_window, height=2)
    for item in ["Homebrew", "Book"]:
        homebrew_listbox.insert(tkinter.END, item)
    homebrew_listbox.grid(row=12, column=3, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)

    #Challange rating rows
    ch_rating_txt = tkinter.Label(add_npc_window, text="Challenge rating:")
    ch_rating_txt.grid(row=17, column=1, sticky=tkinter.W)

    ch_rating_scale = tkinter.Scale(add_npc_window, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    ch_rating_scale.grid(row=17, column=2, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)
    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)

    #CONFRIM BUTTON

    add_monster_btn = tkinter.Button(add_npc_window, text="Add", command=add_npc_to_db)
    add_monster_btn.grid(row=20, column=2)

    # Creature Type Listbox
    add_monster_creature_type_txt = tkinter.Label(add_npc_window, text="Creature Type")
    add_monster_creature_type_txt.grid(row=10, column=3)

    add_monster_creature_type = tkinter.Listbox(add_npc_window, height=17)
    add_monster_creature_type.grid(row=11, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        add_monster_creature_type.insert(tkinter.END, item)




    add_npc_window.mainloop()


def add_monster_win():
    #declare all f*cking variables as global.........
    global add_monster_window
    global w2_txt1
    global w2_txt2_input
    global w2_txt3
    global w2_txt4_input
    global w2_txt5
    global w2_txt6_input
    global w2_txt7
    global w2_txt8_input
    global w2_txt9
    global w2_txt10_input
    global w2_txt11
    global w2_txt12_input
    global w2_txt13
    global w2_txt14_input
    global w2_txt15
    global w2_txt16_input
    global w2_txt17
    global w2_txt18_input
    global w2_txt19
    global w2_txt20_input
    global w2_txt21
    global w2_txt22_input
    global w2_txt23
    global w2_txt24_input
    global homebrew_txt
    global homebrew_listbox
    global ch_rating_txt
    global ch_rating_scale
    global add_monster_btn
    global add_monster_creature_type_txt
    global add_monster_creature_type

    #window stats
    add_monster_window = tkinter.Tk()
    add_monster_window.title("Add Monster")
    add_monster_window.geometry("800x800")
    add_monster_window.resizable(1, 1)

    #add monster stats
    w2_txt1 = tkinter.Label(add_monster_window, text="Name:")
    w2_txt1.grid(row=1, column=1)
    w2_txt2_input = tkinter.Entry(add_monster_window)
    w2_txt2_input.grid(row=1, column=2, sticky=tkinter.W)

    w2_txt3 = tkinter.Label(add_monster_window, text="Armor Class:")
    w2_txt3.grid(row=2, column=1)
    w2_txt4_input = tkinter.Entry(add_monster_window)
    w2_txt4_input.grid(row=2, column=2, sticky=tkinter.W)

    w2_txt5 = tkinter.Label(add_monster_window, text="Hit Points:")
    w2_txt5.grid(row=3, column=1)
    w2_txt6_input = tkinter.Entry(add_monster_window)
    w2_txt6_input.grid(row=3, column=2, sticky=tkinter.W)

    w2_txt7 = tkinter.Label(add_monster_window, text="Speed:")
    w2_txt7.grid(row=4, column=1)
    w2_txt8_input = tkinter.Entry(add_monster_window)
    w2_txt8_input.grid(row=4, column=2, sticky=tkinter.W)

    w2_txt9 = tkinter.Label(add_monster_window, text="STR:")
    w2_txt9.grid(row=5, column=1)
    w2_txt10_input = tkinter.Entry(add_monster_window)
    w2_txt10_input.grid(row=5, column=2, sticky=tkinter.W)

    w2_txt11 = tkinter.Label(add_monster_window, text="DEX:")
    w2_txt11.grid(row=6, column=1)
    w2_txt12_input = tkinter.Entry(add_monster_window)
    w2_txt12_input.grid(row=6, column=2, sticky=tkinter.W)

    w2_txt13 = tkinter.Label(add_monster_window, text="CON:")
    w2_txt13.grid(row=7, column=1)
    w2_txt14_input = tkinter.Entry(add_monster_window)
    w2_txt14_input.grid(row=7, column=2, sticky=tkinter.W)

    w2_txt15 = tkinter.Label(add_monster_window, text="INT:")
    w2_txt15.grid(row=8, column=1)
    w2_txt16_input = tkinter.Entry(add_monster_window)
    w2_txt16_input.grid(row=8, column=2, sticky=tkinter.W)

    w2_txt17 = tkinter.Label(add_monster_window, text="WIS:")
    w2_txt17.grid(row=9, column=1)
    w2_txt18_input = tkinter.Entry(add_monster_window)
    w2_txt18_input.grid(row=9, column=2, sticky=tkinter.W)

    w2_txt19 = tkinter.Label(add_monster_window, text="CHA:")
    w2_txt19.grid(row=10, column=1)
    w2_txt20_input = tkinter.Entry(add_monster_window)
    w2_txt20_input.grid(row=10, column=2, sticky=tkinter.W)

    #this is the two long text box
    w2_txt21 = tkinter.Label(add_monster_window, text="Skills:")
    w2_txt21.grid(row=11, column=1, sticky=tkinter.W)
    w2_txt22_input = tkinter.Text(add_monster_window, height=10, width=50)
    w2_txt22_input.grid(row=11, column=2, sticky=tkinter.W)

    w2_txt23 = tkinter.Label(add_monster_window, text="Actions:")
    w2_txt23.grid(row=12, column=1, sticky=tkinter.W)
    w2_txt24_input = tkinter.Text(add_monster_window, height=10, width=50)
    w2_txt24_input.grid(row=12, column=2, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=13)

    #listbox : homebrew or book

    homebrew_listbox = tkinter.Listbox(add_monster_window, height=2)
    for item in ["Homebrew", "Book"]:
        homebrew_listbox.insert(tkinter.END, item)
    homebrew_listbox.grid(row=12, column=3, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)

    #Challange rating rows
    ch_rating_txt = tkinter.Label(add_monster_window, text="Challenge rating:")
    ch_rating_txt.grid(row=17, column=1, sticky=tkinter.W)

    ch_rating_scale = tkinter.Scale(add_monster_window, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    ch_rating_scale.grid(row=17, column=2, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)
    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)

    #CONFRIM BUTTON

    add_monster_btn = tkinter.Button(add_monster_window, text="Add", command=add_monster_to_db)
    add_monster_btn.grid(row=20, column=2)

    # Creature Type Listbox
    add_monster_creature_type_txt = tkinter.Label(add_monster_window, text="Creature Type")
    add_monster_creature_type_txt.grid(row=10, column=3)

    add_monster_creature_type = tkinter.Listbox(add_monster_window, height=17)
    add_monster_creature_type.grid(row=11, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        add_monster_creature_type.insert(tkinter.END, item)



    add_monster_window.mainloop()

#function for button
def add_monster_to_db():
    #globalling everything...............
    global get_monster_name
    global get_monster_ac
    global get_monster_hp
    global get_monster_speed
    global get_monster_str
    global get_monster_str
    global get_monster_dex
    global get_monster_con
    global get_monster_int
    global get_monster_wis
    global get_monster_cha
    global get_monster_skills
    global get_monster_actions
    global get_monster_homebrew
    global get_monster_challange_rating
    global get_monster_creature_type

    # adding the input values to variables
    get_monster_name = w2_txt2_input.get()
    get_monster_ac = w2_txt4_input.get()
    get_monster_hp = w2_txt6_input.get()
    get_monster_speed = w2_txt8_input.get()
    get_monster_str = w2_txt10_input.get()
    get_monster_dex = w2_txt12_input.get()
    get_monster_con = w2_txt14_input.get()
    get_monster_int = w2_txt16_input.get()
    get_monster_wis = w2_txt18_input.get()
    get_monster_cha = w2_txt20_input.get()
    get_monster_skills = w2_txt22_input.get("1.0",tkinter.END)
    get_monster_actions = w2_txt24_input.get("1.0",tkinter.END)
    get_monster_homebrew = homebrew_listbox.get(tkinter.ACTIVE)
    get_monster_challange_rating = ch_rating_scale.get()
    get_monster_creature_type = add_monster_creature_type.get(tkinter.ACTIVE)

    #connecting to database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()


    c.execute("INSERT INTO monsters (name, ac, hp, speed, str, dex, con, int, wis, cha, skills, actions, challenge_rating, creature_type, homebrew) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (get_monster_name, get_monster_ac, get_monster_hp, get_monster_speed, get_monster_str, get_monster_dex,
         get_monster_con, get_monster_int, get_monster_wis, get_monster_cha, get_monster_skills, get_monster_actions,
         get_monster_challange_rating, get_monster_creature_type, get_monster_homebrew))

    #save and close database
    conn.commit()
    conn.close()

    # printing out that adding was successfully
    add_monster_successfully = tkinter.Label(add_monster_window, text="Adding %s was success." % get_monster_name, fg="red")
    add_monster_successfully.grid(row=21, column=2)


#function for button
def add_npc_to_db():
    # adding the input values to variables
    get_monster_name = w2_txt2_input.get()
    get_monster_ac = w2_txt4_input.get()
    get_monster_hp = w2_txt6_input.get()
    get_monster_speed = w2_txt8_input.get()
    get_monster_str = w2_txt10_input.get()
    get_monster_dex = w2_txt12_input.get()
    get_monster_con = w2_txt14_input.get()
    get_monster_int = w2_txt16_input.get()
    get_monster_wis = w2_txt18_input.get()
    get_monster_cha = w2_txt20_input.get()
    get_monster_skills = w2_txt22_input.get("1.0", tkinter.END)
    get_monster_actions = w2_txt24_input.get("1.0", tkinter.END)
    get_monster_homebrew = homebrew_listbox.get(tkinter.ACTIVE)
    get_monster_challange_rating = ch_rating_scale.get()
    get_monster_creature_type = add_monster_creature_type.get(tkinter.ACTIVE)

    #connecting to database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    # creating table...
    #c.execute("""CREATE TABLE npc (name, ac, hp, speed, str, dex, con, int, wis,
                #cha, skills, actions, challenge_rating, creature_type, homebrew)""")

    c.execute("INSERT INTO npc (name, ac, hp, speed, str, dex, con, int, wis, cha, skills, actions, challenge_rating, creature_type, homebrew) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (get_monster_name, get_monster_ac, get_monster_hp, get_monster_speed, get_monster_str, get_monster_dex,
         get_monster_con, get_monster_int, get_monster_wis, get_monster_cha, get_monster_skills, get_monster_actions,
         get_monster_challange_rating, get_monster_creature_type, get_monster_homebrew))

    for row in c.execute("SELECT rowid, name, speed FROM monsters WHERE homebrew = 'Homebrew'"):
        print(row)

    #save and close database
    conn.commit()
    conn.close()

    # printing out that adding was successfully
    add_monster_successfully = tkinter.Label(add_npc_window, text="Adding %s was success." % get_monster_name,
                                             fg="red")
    add_monster_successfully.grid(row=21, column=2)


    #print(get_monster_name,get_monster_ac,get_monster_hp,get_monster_speed,
    #      get_monster_str, get_monster_dex, get_monster_con, get_monster_int,
    #      get_monster_wis, get_monster_cha)
    #print()
    #print(get_monster_skills, get_monster_actions)
    #
    #print(str(type(get_monster_name))+"("+get_monster_name+")")
    #
    #print("homebrew: "+ str(get_monster_homebrew))
    #print("challange rating: "+str(get_monster_challange_rating))
    #print("creature type: "+str(get_monster_creature_type))



#-------------------------------------------- GENERATE FIGHT ------------------------------------------------

#GENERATE FIGHT ---> BUTTON FUNCTIONS

#---------ADD CHARACTER BUTTON
def gen_fight_char_button_f():
    global generate_fight_character
    generate_fight_character = tkinter.Tk()
    generate_fight_character.title("Add Character")

    gen_fight_char_top = tkinter.Label(generate_fight_character, text="Choose one of the following opportunities, than click -Add-")
    gen_fight_char_top.grid(row=1, column=1)

    #connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    #make the table empty:
    c.execute("DELETE FROM fighting_char WHERE rowid > 0")
    #save and close database
    conn.commit()
    conn.close()

    #create the listbox of characters:
    global gen_fight_char_listbox
    gen_fight_char_listbox = tkinter.Listbox(generate_fight_character, height=6, selectbackground="purple")
    gen_fight_char_listbox.grid(row=3, column=1)

    #fill the listbox
    for item in ["Putukas", "Shadow Fury", "Farvizes Sallango", "Ped Ophelia", "Stickee", "Crag Stone"]:
        gen_fight_char_listbox.insert(tkinter.END, item)



    #ADD ALL button
    gen_fight_char_addall_button = tkinter.Button(generate_fight_character, text="ADD ALL", bg="blue", fg="white", command=gen_fight_char_add_all_button_f)
    gen_fight_char_addall_button.grid(row=5, column=1)
    #ADD button
    gen_fight_char_add_button = tkinter.Button(generate_fight_character, text="ADD active", bg="green", fg="black", command=gen_fight_char_add_button_f)
    gen_fight_char_add_button.grid(row=4, column=1)

    #instructions for adding characters

    add_char_instructions = tkinter.Label(generate_fight_character, text="Add characters to the fight one by one, or add all of them in one click. If you fail, just destroy this window and reopen it.", fg="red")
    add_char_instructions.grid(row=2, column=1)

#function for the "ADD ALL" button in the add character window
def gen_fight_char_add_all_button_f():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    for all_fight in ["Putukas", "Shadow Fury", "Farvizes Sallango", "Ped Ophelia", "Stickee", "Crag Stone"]:
        c.execute("INSERT OR IGNORE INTO fighting_char (name) VALUES (?)", (all_fight,))
    # save and close database
    conn.commit()
    conn.close()

    adding_all_was_success1 = tkinter.Label(generate_fight_character, text="Adding all from list was success. You can destroy this window.", fg="green")
    adding_all_was_success1.grid(row=6, column=1)

#function for the "ADD" button in the add character window
def gen_fight_char_add_button_f():
    #get the value:
    global gen_fight_char_value
    gen_fight_char_value = gen_fight_char_listbox.get(tkinter.ACTIVE)
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO fighting_char (name) VALUES (?)", (gen_fight_char_value,))
    #save and close database
    conn.commit()
    conn.close()

    adding_char_was_success = tkinter.Label(generate_fight_character, text="Adding %s was success." % gen_fight_char_value, fg="green")
    adding_char_was_success.grid(row=7, column=1)
# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz
#---------ADD MONSTER BUTTON
def gen_fight_monster_button_f():
    generate_fight_monster = tkinter.Tk()
    generate_fight_monster.title("Add monster to the fight")
    generate_fight_monster.geometry("1600x900")

    gen_fight_monster_search = tkinter.Label(generate_fight_monster, text="Search for monsters!")
    gen_fight_monster_search.grid(row=1, column=1)

    # clearing the database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("DELETE FROM fighting_mon WHERE rowid > 0")
    conn.commit()
    conn.close()

    #searching by name:
    gen_fight_monster_search_name = tkinter.Label(generate_fight_monster, text="Name")
    gen_fight_monster_search_name.grid(row=2, column=1)
    global gen_fight_monster_search_name_entry
    gen_fight_monster_search_name_entry = tkinter.Entry(generate_fight_monster)
    gen_fight_monster_search_name_entry.grid(row=2, column=2)
    gen_fight_monster_search_name_button = tkinter.Button(generate_fight_monster, text="Search by name", command=gen_fight_search_name_button_f)
    gen_fight_monster_search_name_button.grid(row=2, column=3)

    #empty row:
    gen_fight_monster_empty = tkinter.Label(generate_fight_monster)
    gen_fight_monster_empty.grid(row=3, column=1)

    #searching by challange rating:
    global gen_fight_monster_search_cr_scale
    gen_fight_monster_search_cr = tkinter.Label(generate_fight_monster, text="Challange Rating")
    gen_fight_monster_search_cr.grid(row=4, column=1)
    gen_fight_monster_search_cr_scale = tkinter.Scale(generate_fight_monster, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    gen_fight_monster_search_cr_scale.grid(row=4, column=2, sticky=tkinter.W)
    gen_fight_monster_search_cr_button = tkinter.Button(generate_fight_monster, text="Search by CR", command=gen_fight_search_cr_button_f)
    gen_fight_monster_search_cr_button.grid(row=4, column=3)


    #searching by creature type
    gen_fight_monster_search_ct = tkinter.Label(generate_fight_monster, text="Creature Type")
    gen_fight_monster_search_ct.grid(row=6, column=1)
    global gen_fight_monster_search_ct_listbox
    gen_fight_monster_search_ct_listbox = tkinter.Listbox(generate_fight_monster, height=17)
    gen_fight_monster_search_ct_listbox.grid(row=6, column=2)
    gen_fight_monster_search_ct_button = tkinter.Button(generate_fight_monster, text="Search by CT", command=gen_fight_search_ct_button_f)
    gen_fight_monster_search_ct_button.grid(row=6, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        gen_fight_monster_search_ct_listbox.insert(tkinter.END, item)

#function for the "search by name" button
def gen_fight_search_name_button_f():

    global gen_fight_search_name_value
    gen_fight_search_name_value = gen_fight_monster_search_name_entry.get()

    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE name LIKE (? || '%')", (gen_fight_search_name_value,))


    monsters_name_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_name_list.append(to_the_list[0])

    global search_mon_byname
    search_mon_byname = tkinter.Tk()
    search_mon_byname.title("Search Monster by NAME")
    search_mon_byname.geometry("400x400")

    global searched_monsters_name
    searched_monsters_name = tkinter.Listbox(search_mon_byname, height=len(monsters_name_list))
    searched_monsters_name.grid(row=1, column=1)
    for item in monsters_name_list:
        searched_monsters_name.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_byname, text="ADD", command=add_monster_to_fight_by_name)
    searched_monsters_add_button.grid(row=2, column=2)


# function to the ADD button in search monsters by name window
def add_monster_to_fight_by_name():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_name.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_byname, text="Adding %s to the fight was success." % searched_monster_todb, fg="blue").grid(row=4, column=1)




#function for the "search by challange rating" button
def gen_fight_search_cr_button_f():
    global gen_fight_monster_search_cr_value
    gen_fight_monster_search_cr_value = gen_fight_monster_search_cr_scale.get()
    #connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE challenge_rating=?", (gen_fight_monster_search_cr_value,))

    monsters_cr_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_cr_list.append(to_the_list[0])

    global search_mon_bycr
    search_mon_bycr = tkinter.Tk()
    search_mon_bycr.title("Search Monster by Challange Rating")
    search_mon_bycr.geometry("400x400")

    global searched_monsters_cr
    searched_monsters_cr = tkinter.Listbox(search_mon_bycr, height=len(monsters_cr_list))
    searched_monsters_cr.grid(row=1, column=1)
    for item in monsters_cr_list:
        searched_monsters_cr.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_bycr, text="ADD", command=add_monster_to_fight_by_cr)
    searched_monsters_add_button.grid(row=2, column=2)


# function to the ADD button in monsters searching by challange rating
def add_monster_to_fight_by_cr():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_cr.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_bycr, text= "Adding %s to the fight was success." %searched_monster_todb, fg="blue").grid(row=4, column=1)


# function for the "search by creature type" button
def gen_fight_search_ct_button_f():
    global gen_fight_monster_search_ct_value
    gen_fight_monster_search_ct_value = gen_fight_monster_search_ct_listbox.get(tkinter.ACTIVE)


    # connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE creature_type=?", (gen_fight_monster_search_ct_value,))

    monsters_ct_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_ct_list.append(to_the_list[0])

    global search_mon_byct
    search_mon_byct = tkinter.Tk()
    search_mon_byct.title("Search Monster by Challange Rating")
    search_mon_byct.geometry("400x400")

    global searched_monsters_ct
    searched_monsters_ct = tkinter.Listbox(search_mon_byct, height=len(monsters_ct_list))
    searched_monsters_ct.grid(row=1, column=1)
    for item in monsters_ct_list:
        searched_monsters_ct.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_byct, text="ADD", command=add_monster_to_fight_by_ct)
    searched_monsters_add_button.grid(row=2, column=2)


def add_monster_to_fight_by_ct():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_ct.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_byct, text="Adding %s to the fight was success." % searched_monster_todb, fg="blue").grid(row=4, column=1)

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz
#---------ADD NPC BUTTON
def gen_fight_npc_button_f():
    generate_fight_npc = tkinter.Tk()
    generate_fight_npc.title("Add NPC to the fight")
    generate_fight_npc.geometry("1600x900")

    gen_fight_npc_search = tkinter.Label(generate_fight_npc, text="Search for NPC!")
    gen_fight_npc_search.grid(row=1, column=1)

    # clearing the database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("DELETE FROM fighting_npc WHERE rowid > 0")
    conn.commit()
    conn.close()

    #searching by name:
    gen_fight_npc_search_name = tkinter.Label(generate_fight_npc, text="Name")
    gen_fight_npc_search_name.grid(row=2, column=1)
    global gen_fight_npc_search_name_entry
    gen_fight_npc_search_name_entry = tkinter.Entry(generate_fight_npc)
    gen_fight_npc_search_name_entry.grid(row=2, column=2)
    gen_fight_npc_search_name_button = tkinter.Button(generate_fight_npc, text="Search by name", command=gen_fight_search_name_button_f_npc)
    gen_fight_npc_search_name_button.grid(row=2, column=3)

    #empty row:
    gen_fight_npc_empty = tkinter.Label(generate_fight_npc)
    gen_fight_npc_empty.grid(row=3, column=1)

    #searching by challange rating:
    global gen_fight_npc_search_cr_scale
    gen_fight_npc_search_cr = tkinter.Label(generate_fight_npc, text="Challange Rating")
    gen_fight_npc_search_cr.grid(row=4, column=1)
    gen_fight_npc_search_cr_scale = tkinter.Scale(generate_fight_npc, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    gen_fight_npc_search_cr_scale.grid(row=4, column=2, sticky=tkinter.W)
    gen_fight_npc_search_cr_button = tkinter.Button(generate_fight_npc, text="Search by CR", command=gen_fight_search_cr_button_f_npc)
    gen_fight_npc_search_cr_button.grid(row=4, column=3)


    #searching by creature type
    gen_fight_npc_search_ct = tkinter.Label(generate_fight_npc, text="Creature Type")
    gen_fight_npc_search_ct.grid(row=6, column=1)
    global gen_fight_npc_search_ct_listbox
    gen_fight_npc_search_ct_listbox = tkinter.Listbox(generate_fight_npc, height=17)
    gen_fight_npc_search_ct_listbox.grid(row=6, column=2)
    gen_fight_npc_search_ct_button = tkinter.Button(generate_fight_npc, text="Search by CT", command=gen_fight_search_ct_button_f_npc)
    gen_fight_npc_search_ct_button.grid(row=6, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        gen_fight_npc_search_ct_listbox.insert(tkinter.END, item)

#function for the "search by name" button
def gen_fight_search_name_button_f_npc():

    global gen_fight_search_name_value
    gen_fight_search_name_value = gen_fight_npc_search_name_entry.get()

    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE name LIKE (? || '%')", (gen_fight_search_name_value,))


    npc_name_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_name_list.append(to_the_list[0])

    global search_npc_byname
    search_npc_byname = tkinter.Tk()
    search_npc_byname.title("Search NPC by NAME")
    search_npc_byname.geometry("400x400")

    global searched_npc_name
    searched_npc_name = tkinter.Listbox(search_npc_byname, height=len(npc_name_list))
    searched_npc_name.grid(row=1, column=1)
    for item in npc_name_list:
        searched_npc_name.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_byname, text="ADD", command=add_npc_to_fight_by_name)
    searched_npc_add_button.grid(row=2, column=2)


# function to the ADD button in search monsters by name window
def add_npc_to_fight_by_name():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_name.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_byname, text="Adding %s to the fight was success." % searched_npc_todb, fg="blue").grid(row=4, column=1)




#function for the "search by challange rating" button
def gen_fight_search_cr_button_f_npc():
    global gen_fight_npc_search_cr_value
    gen_fight_npc_search_cr_value = gen_fight_npc_search_cr_scale.get()
    #connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE challenge_rating=?", (gen_fight_npc_search_cr_value,))

    npc_cr_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_cr_list.append(to_the_list[0])

    global search_npc_bycr
    search_npc_bycr = tkinter.Tk()
    search_npc_bycr.title("Search NPC by Challange Rating")
    search_npc_bycr.geometry("400x400")

    global searched_npc_cr
    searched_npc_cr = tkinter.Listbox(search_npc_bycr, height=len(npc_cr_list))
    searched_npc_cr.grid(row=1, column=1)
    for item in npc_cr_list:
        searched_npc_cr.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_bycr, text="ADD", command=add_npc_to_fight_by_cr)
    searched_npc_add_button.grid(row=2, column=2)


# function to the ADD button in monsters searching by challange rating
def add_npc_to_fight_by_cr():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_cr.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_bycr, text= "Adding %s to the fight was success." %searched_npc_todb, fg="blue").grid(row=4, column=1)


# function for the "search by creature type" button
def gen_fight_search_ct_button_f_npc():
    global gen_fight_npc_search_ct_value
    gen_fight_npc_search_ct_value = gen_fight_npc_search_ct_listbox.get(tkinter.ACTIVE)


    # connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE creature_type=?", (gen_fight_npc_search_ct_value,))

    npc_ct_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_ct_list.append(to_the_list[0])

    global search_npc_byct
    search_npc_byct = tkinter.Tk()
    search_npc_byct.title("Search NPC by Challange Rating")
    search_npc_byct.geometry("400x400")

    global searched_npc_ct
    searched_npc_ct = tkinter.Listbox(search_npc_byct, height=len(npc_ct_list))
    searched_npc_ct.grid(row=1, column=1)
    for item in npc_ct_list:
        searched_npc_ct.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_byct, text="ADD", command=add_npc_to_fight_by_ct)
    searched_npc_add_button.grid(row=2, column=2)


def add_npc_to_fight_by_ct():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_ct.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_byct, text="Adding %s to the fight was success." % searched_npc_todb, fg="blue").grid(row=4, column=1)

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz













# function for the SHOW ADDED button
def gen_fight_show_added_f():
    #clean the shit
    for w in range(15):
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=3)
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=4)
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=5)


    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("SELECT * FROM fighting_char")
    fake_list = []
    global real_list
    real_list = []
    fighting_chars = c.fetchall()
    for item in fighting_chars:
        fake_list.append(item)
    if ("Putukas",) in fake_list:
        real_list.append("Putukas")
    if ("Shadow Fury",) in fake_list:
        real_list.append("Shadow Fury")
    if ("Farvizes Sallango",) in fake_list:
        real_list.append("Farvizes Sallango")
    if ("Ped Ophelia",) in fake_list:
        real_list.append("Ped Ophelia")
    if ("Stickee",) in fake_list:
        real_list.append("Stickee")
    if ("Crag Stone",) in fake_list:
        real_list.append("Crag Stone")
    #this belows prints out the added characters when SHOW ADD button is clicked
    for i in range(len(real_list)):
        tkinter.Label(generate_fight_win, text="ADDED:", bg="black", fg="white").grid(row=1, column=2)
        tkinter.Label(generate_fight_win, text="Characters:", fg="blue").grid(row=1, column=3)
        gen_fight_show_added_chars = tkinter.Label(generate_fight_win, text="{}".format(real_list[i]))
        gen_fight_show_added_chars.grid(row=i+2, column=3)


    monsters_fighting = c.execute("SELECT * FROM fighting_mon")
    real_list2=[]
    for names in monsters_fighting:
        real_list2.append(names)

    for j in range(len(real_list2)):
        tkinter.Label(generate_fight_win, text="Monsters:", fg="blue").grid(row=1, column=4)
        print_the_monster = tkinter.Label(generate_fight_win, text="%s" % (real_list2[j]))
        print_the_monster.grid(row=j+2, column=4)

    npc_fighting = c.execute("SELECT * FROM fighting_npc")
    real_list3 = []
    for names_npc in npc_fighting:
        real_list3.append(names_npc)

    for k in range(len(real_list3)):
        tkinter.Label(generate_fight_win, text="NPC:", fg="blue").grid(row=1, column=5)
        print_the_npc = tkinter.Label(generate_fight_win, text="%s" % (real_list3[k]))
        print_the_npc.grid(row=k + 2, column=5)



#MAIN WINDOW
def generate_fight_window():
    # window stats
    global generate_fight_win
    generate_fight_win = tkinter.Tk()
    generate_fight_win.title("Generate Fight")
    generate_fight_win.geometry("1600x900")
    #generate_fight_win.attributes("-fullscreen", True)
    #generate_fight_win.attributes("-fullscreen", False)


    gen_fight_top = tkinter.Label(generate_fight_win, text="Adding the need to the fight...", fg="blue")
    gen_fight_top.grid(row=1, column=1)

    gen_fight_top_under = tkinter.Label(generate_fight_win, text="What do you want to add to the fight?")
    gen_fight_top_under.grid(row=2, column=1)


    #Buttons for adding:

    gen_fight_char_button = tkinter.Button(generate_fight_win, text="Character", bg="green", fg="white", command=gen_fight_char_button_f)
    gen_fight_char_button.grid(row=3, column=1)

    gen_fight_monster_button = tkinter.Button(generate_fight_win, text="Monster", bg="red", fg="white", command=gen_fight_monster_button_f)
    gen_fight_monster_button.grid(row=4, column=1)

    gen_fight_npc_button = tkinter.Button(generate_fight_win, text="NPC", bg="blue", fg="white", command=gen_fight_npc_button_f)
    gen_fight_npc_button.grid(row=5, column=1)

    gen_fight_show_added_button = tkinter.Button(generate_fight_win, text="Show added", bg="white", fg="black", command=gen_fight_show_added_f)
    gen_fight_show_added_button.grid(row=6, column=1)

    gen_fight_continue_button = tkinter.Button(generate_fight_win, text="Continue", command=continute_to_initiative)
    gen_fight_continue_button.grid(row=999, column=999)

    #some space column between buttons

    gen_fight_empty1 = tkinter.Label(generate_fight_win)
    gen_fight_empty1.grid(row=7, column=1)



# "CONTINUE" BUTTON FUNCTION to the initiative

def continute_to_initiative():

    initiative_window = tkinter.Tk()
    initiative_window.title("Giving Initiatives")
    initiative_window.geometry("300x900")

    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    s = c.execute("SELECT name FROM fighting_char")
    fighting_character_list = []
    for row in s:
        fighting_character_list.append(row)

    tkinter.Label(initiative_window, text="Initiatives:", fg="blue").grid(row=1, column=2)
    for i in range(len(fighting_character_list)):
        tkinter.Label(initiative_window, text="%s" % (fighting_character_list[i])).grid(row=(i+2), column=1)

    char_dict = [[],
                 []]

    for j in range(len(fighting_character_list)):
        char_dict[0].append(fighting_character_list[j])
        char_dict[1].append("tkinter.Entry(initiative_window).grid(row=(i+1)*2, column=2)")

    for k in range(5):
        globals()['cat_%s' % k] = k

    print(cat_1, cat_1, cat_2, cat_3, cat_4)

    # ezt itt folul muszaj folytatni ez igy tud mukodni!!!!!!
    #ez a globals() cucc olyat tud, hogy egy loopon belul tobb kulonbozo valtozot hozol letre...
    # ez itt nekunk azert jo, mert igy megcsinalhatjuk a kezdemenyezos ablakot
    # egy oszlop karakter, mellette a tkinter.Entry cuccos, es az entrynek hozunk letre valtozot ezzel a globals() funkcioval
    # pl:
    #for i in range(len(fighting_character_list)):
    #    tkinter.Label(initiative_window, text="%s" % (fighting_character_list[i])).grid(row=i+1, column=1)
    #    globals()['char_init_entry_%s' % i+1] = tkinter.Entry(initiative_window).grid(row=(i+2) , column=2)
    #    globals()['char_init_entry_get_%s' % i+1] = globals()['char_init_entry_%s' % i+1].get()




main_win()
