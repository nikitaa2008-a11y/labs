print("Замок дракона")
print("Соберите доспех и меч, победите дракона")
print("Введите help для просмотра списка команд")

#начальные сведения
room = "gate"
hp = 100
has_armor = False
has_sword = False
game_over = False

sword_forge = True
armor_treasure = True

print("|gate| Вы у ворот замка. На севере - двор")
print()

while not game_over:
    command = input("> ").strip().lower()

    #help
    if command == "help":
        print("доступные команды:")
        print("use (использовать предмет)")
        print("go <direction> (идти в направлении)")
        print("look (осмотреть помещение на начличие предметов)")
        print("take <sword or armor> (взять предмет)")
        print("fight (доступно в логвое дракона)")
        print("exit (выйти из игры)")
        print()

    elif command == "":
        continue

    #look
    elif command == "look":
        if room == "gate":
            print("|gate| Вы у ворот замка. На севере - двор")
        elif room == "yard":
            print("|yard| Вы во дворе замка. На восток - кузница, запад - башня, север - логово дракона")
        elif room == "forge":
            print("|forge| Вы в кузнице. На западе выход во двор ")
            if sword_forge is True:
                print("Вы видите на одной из полок старый закаленный меч")
        elif room == "tower":
            print("|tower| Вы в башне. Наверху сокровищница, на вотоке двор")
        elif room == "treasury":
            print("Вы в сокровищнице. Вниз - башня")
            if armor_treasure is True:
                print("Вы видите старую кирасу")
        elif room == "lair":
            print("|lair| Вы в логове дракона! Дракон здесь. На юге - двор")
            print("Дракон угрожающе смотрит на Вас")
        print()

    #go
    elif command.startswith("go "):
        direction = command[3:].strip().lower()
        new_room = room
        moved = False

        if room == "gate":
            if direction == "north":
                new_room = "yard"
                moved = True
        elif room == "yard":
            if direction == "south":
                new_room = "gate"
                moved = True
            elif direction == "east":
                new_room = "forge"
                moved = True
            elif direction == "west":
                new_room = "tower"
                moved = True
            elif direction == "north":
                new_room = "lair"
                moved = True
        elif room == "forge":
            if direction == "west":
                new_room = "yard"
                moved = True
        elif room == "tower":
            if direction == "up":
                new_room = "treasury"
                moved = True
            elif direction == "east":
                new_room = "yard"
                moved = True
        elif room == "treasury":
            if direction == "down":
                new_room = "tower"
                moved = True
        elif room == "lair":
            if direction == "south":
                new_room = "yard"
                moved = True

        if moved is False:
            print(f"Нельзя пройти {direction} из {room}. ")
        else:
            room = new_room
            if room == "gate":
                print("|gate| Вы у ворот замка. На севере - двор")
            elif room == "yard":
                print("|yard| Вы во дворе замка. На восток - кузница, запад - башня, север - логово дракона")
            elif room == "forge":
                print("|forge| Вы в кузнице. На западе выход во двор ")
                if sword_forge is True:
                    print("Вы видите на одной из полок старый закаленный меч")
            elif room == "tower":
                print("|tower| Вы в башне. Наверху сокровищница, на вотоке двор")
            elif room == "treasury":
                print("Вы в сокровищнице. Вниз - башня")
                if armor_treasure is True:
                    print("Вы видите старую кирасу")
            elif room == "lair":
                print("|lair| Вы в логове дракона! Дракон здесь. На юге - двор")
                print("Дракон угрожающе смотрит на Вас")
            print()

    #take
    elif command.startswith("take "):
        item = command[4:].strip().lower()
        if room == "forge" and item == "sword" and sword_forge:
            sword_forge = False
            has_sword = True
            print("Вы взяли меч.")
        elif room == "treasury" and item == "armor" and armor_treasure:
            armor_treasure = False
            has_armor = True
            print("Вы взяли кирасу")
        else:
            print(f"здесь нет предмета {item}.") 

    #use
    elif command.startswith("use "):
        item = command[4:].strip().lower()
        if item == "sword" and has_sword:
            print("вы используете меч (ничего не происходит)")
        elif item == "armor" and has_armor:
            print("вы используете кирасу (ничего не проиходит)")
        else:
            print(f"у Вас нет {item}.") 

    #fight
    elif command == "fight":
        if room != "lair":
            print("тут не с кем сражаться")
        elif has_armor and has_sword:
            print("Вы даете бой дракону...")
            print("Дракон повержен. Победа!")
            game_over = True
        else:
            hp = hp - 30
            print("Дракон атакует Вас!")
            print("Вы теряете 30 hp")
            print(f"Осталось hp:{hp}.")
            if hp <= 0:
                print("Вы погибли! Поражение.")
                game_over = True 

            
    elif command == "exit":
        print("выход из игры")
        game_over = True
    
    else:
        print(f"неизвестная команда '{command}', введите help для просмотра доступных команд")

print()
print("игра завершена")        

    
