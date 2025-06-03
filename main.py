def on_up_pressed():
    animation.run_image_animation(Link,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    global Current_level
    Current_level += 1
    Change_Level(Current_level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_south,
    on_overlap_tile)

def on_b_pressed():
    global Arrow
    Arrow = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . 1 1 . . . . . . . . . . . . . 
                    . . . 1 1 1 . . . . . . . . . . 
                    . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                    . . . . . . . . . . . 1 1 . . . 
                    . . . 1 1 1 e e e e e e 1 1 . . 
                    . . . f f f f f f f f 1 1 f . . 
                    . . . . . . . . 1 1 1 f f . . . 
                    . 1 1 1 1 1 1 1 1 . . . . . . . 
                    . . . . 1 1 1 . . . . . . . . . 
                    . 1 1 1 1 . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Link,
        50,
        0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global Sword
    Sword = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . 1 f . . . 
                    . . . . . . . . . . . . f . . . 
                    . . . . . . . . . . . 1 f . . . 
                    . . . . . . . . . . . . f . . . 
                    . . . . . . . . . . . . f . . . 
                    . . . . . . . . . . . 1 f . . . 
                    . . . . . . . . . . 1 f . . . . 
                    . . . . . . . . . . f . . . . . 
                    . . . . . . . . . 1 f . . . . . 
                    . . . . . . . . 1 f . . . . . . 
                    . . . . . . 1 f f . . . . . . . 
                    1 . . 1 . 1 f . . . . . . . . . 
                    f f f f f f . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Link,
        50,
        0)
    pause(200)
    sprites.destroy(Sword)
    animation.run_image_animation(Link,
        [img("""
                ........................
                        ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef...cc.......
                        .ffffee2222ef.cdc.......
                        .fe222ffffe2fcddc.......
                        fffffffeeeffcddc........
                        ffe44ebf44ecddc.........
                        fee4d41fddecdc..........
                        .feee4dddedccc..........
                        ..ffee44e4dde...........
                        ...f222244ee............
                        ...f2222e2f.............
                        ...f444455f.............
                        ....ffffff..............
                        .....fff................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        .......fff..............
                        ....fffff2f.............
                        ..ffeeeee22ff...........
                        .ffeeeeee222ff..........
                        .feeeefffeeeef..........
                        .fffffeee2222ef.........
                        fffe222fffffe2f.........
                        fffffffffeeefff.....cc..
                        fefe44ebbf44eef...ccdc..
                        .fee4d4bbfddef..ccddcc..
                        ..feee4dddddfeecdddc....
                        ...f2222222eeddcdcc.....
                        ...f444445e44ddccc......
                        ...ffffffffeeee.........
                        ...fff...ff.............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                .......ff...............
                        ....ffff2ff.............
                        ..ffeeeef2ff............
                        .ffeeeeef22ff...........
                        .feeeeffeeeef...........
                        .fffffee2222ef..........
                        fffe222ffffe2f..........
                        ffffffffeeefff..........
                        fefe44ebf44eef..........
                        .fee4d4bfddef...........
                        ..feee4dddee.c..........
                        ...f2222eeddeccccccc....
                        ...f444e44ddecddddd.....
                        ...fffffeeee.ccccc......
                        ..ffffffff...c..........
                        ..fff..ff...............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef............
                        .ffffee2222ef...........
                        .fe222ffffe2f...........
                        fffffffeeefff...........
                        ffe44ebf44eef...........
                        fee4d41fddef............
                        .feee4ddddf.............
                        ..fdde444ef.............
                        ..fdde22ccc.............
                        ...eef22cdc.............
                        ...f4444cddc............
                        ....fffffcddc...........
                        .....fff..cddc..........
                        ...........cdc..........
                        ............cc..........
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        100,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    pass
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_overlap_tile2(sprite2, location2):
    global Current_level
    Current_level += 1
    Change_Level(Current_level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_east,
    on_overlap_tile2)

def on_left_pressed():
    animation.run_image_animation(Link,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 2 2 2 2 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile3(sprite3, location3):
    global Current_level
    Current_level += 1
    Change_Level(Current_level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_west,
    on_overlap_tile3)

def on_on_zero(status):
    sprites.destroy(status.sprite_attached_to(), effects.disintegrate, 500)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def Change_Level(Level_Number: number):
    if Level_Number == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
    elif Level_Number == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
    elif Level_Number == 3:
        tiles.set_current_tilemap(tilemap("""
            level12
        """))
    elif Level_Number == 4:
        tiles.set_current_tilemap(tilemap("""
            level14
        """))
    elif Level_Number == 5:
        tiles.set_current_tilemap(tilemap("""
            level17
        """))
    elif Level_Number == 6:
        tiles.set_current_tilemap(tilemap("""
            level19
        """))
    elif Level_Number == 7:
        tiles.set_current_tilemap(tilemap("""
            level21
        """))
    elif Level_Number == 8:
        tiles.set_current_tilemap(tilemap("""
            level23
        """))
        scene.set_background_color(7)
    elif Level_Number == 9:
        tiles.set_current_tilemap(tilemap("""
            level23
        """))
        scene.set_background_color(7)
    elif Level_Number == 10:
        tiles.set_current_tilemap(tilemap("""
            level29
        """))
        scene.set_background_color(4)
    elif Level_Number == 11:
        tiles.set_current_tilemap(tilemap("""
            level32
        """))
    tiles.place_on_random_tile(Link, sprites.dungeon.floor_light0)
def Reset_Sprite(Animation: number):
    if Animation == 0:
        animation.stop_animation(animation.AnimationTypes.ALL, Link)

def on_right_pressed():
    animation.run_image_animation(Link,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 2 2 2 2 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(Link,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 2 2 2 2 e d d 4 e . . 
                        . . e 4 f 2 2 2 2 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile4(sprite4, location4):
    global Current_level
    Current_level += 1
    Change_Level(Current_level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_west,
    on_overlap_tile4)

def on_on_overlap(sprite5, otherSprite):
    sprites.destroy(sprite5)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite).value += -16
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite6, otherSprite2):
    sprites.destroy(otherSprite2, effects.halo, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Ghoul: Sprite = None
statusbar: StatusBarSprite = None
Snake: Sprite = None
Sword: Sprite = None
Arrow: Sprite = None
Current_level = 0
Link: Sprite = None
Link = sprites.create(img("""
        ......ffff..............
            ....fff22fff............
            ...fff2222fff...........
            ..fffeeeeeefff..........
            ..ffe222222eef..........
            ..fe2ffffff2ef..........
            ..ffffeeeeffff......ccc.
            .ffefbf44fbfeff....cddc.
            .ffefbf44fbfeff...cddc..
            .fee4dddddd4eef.ccddc...
            fdfeeddddd4eeffecddc....
            fbffee4444ee4fddccc.....
            fbf4f222222f1edde.......
            fcf.f222222f44ee........
            .ff.f445544f............
            ....ffffffff............
            .....ff..ff.............
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
controller.move_sprite(Link)
scene.set_background_color(0)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
Current_level = 1
Change_Level(1)
scene.camera_follow_sprite(Link)
info.change_life_by(3)

def on_update_interval():
    global Snake, statusbar
    if Current_level == 10:
        Snake = sprites.create(img("""
                . . . . c c c c c c . . . . . . 
                            . . . c 6 7 7 7 7 6 c . . . . . 
                            . . c 7 7 7 7 7 7 7 7 c . . . . 
                            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                            . . f 7 7 7 7 6 c 7 7 6 f c . . 
                            . . . f c c c c 7 7 6 f 7 7 c . 
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.enemy)
        Snake.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Snake)
        animation.run_image_animation(Snake,
            [img("""
                    . . . . c c c c c c . . . . . . 
                                . . . c 6 7 7 7 7 6 c . . . . . 
                                . . c 7 7 7 7 7 7 7 7 c . . . . 
                                . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                                . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                                . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                                . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                                . . f 7 7 7 7 6 c 7 7 6 f c . . 
                                . . . f c c c c 7 7 6 f 7 7 c . 
                                . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                                . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                                c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                                f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                                f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                                . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                                . . c c c c c c c c c f . . . .
                """),
                img("""
                    . . . c c c c c c . . . . . . . 
                                . . c 6 7 7 7 7 6 c . . . . . . 
                                . c 7 7 7 7 7 7 7 7 c . . . . . 
                                c 6 7 7 7 7 7 7 7 7 6 c . . . . 
                                c 7 c 6 6 6 6 c 7 7 7 c . . . . 
                                f 7 6 f 6 6 f 6 7 7 7 f . . . . 
                                f 7 7 7 7 7 7 7 7 7 7 f . . . . 
                                . f 7 7 7 7 6 c 7 7 6 f . . . . 
                                . . f c c c c 7 7 6 f c c c . . 
                                . . c 6 2 7 7 7 f c c 7 7 7 c . 
                                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c 
                                . c 1 1 1 1 7 6 6 c 6 6 6 c c c 
                                . c 1 1 1 1 1 6 6 6 6 6 6 c . . 
                                . c 6 1 1 1 1 1 6 6 6 6 6 c . . 
                                . . c 6 1 1 1 1 1 7 6 6 c c . . 
                                . . . c c c c c c c c c c . . .
                """)],
            100,
            False)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global Ghoul, statusbar
    if Current_level == 10:
        Ghoul = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        Ghoul.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Ghoul)
game.on_update_interval(5000, on_update_interval2)

def on_update_interval3():
    global Ghoul, statusbar
    if Current_level == 4:
        Ghoul = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        Ghoul.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Ghoul)
game.on_update_interval(5000, on_update_interval3)

def on_update_interval4():
    global Ghoul, statusbar
    if Current_level == 11:
        Ghoul = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        Ghoul.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Ghoul)
game.on_update_interval(5000, on_update_interval4)

def on_update_interval5():
    global Ghoul, statusbar
    if Current_level == 3:
        Ghoul = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        Ghoul.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Ghoul)
game.on_update_interval(5000, on_update_interval5)

def on_update_interval6():
    global Snake, statusbar
    if Current_level == 7:
        Snake = sprites.create(img("""
                . . . . c c c c c c . . . . . . 
                            . . . c 6 7 7 7 7 6 c . . . . . 
                            . . c 7 7 7 7 7 7 7 7 c . . . . 
                            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                            . . f 7 7 7 7 6 c 7 7 6 f c . . 
                            . . . f c c c c 7 7 6 f 7 7 c . 
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.enemy)
        Snake.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Snake)
        animation.run_image_animation(Snake,
            [img("""
                    . . . . c c c c c c . . . . . . 
                                . . . c 6 7 7 7 7 6 c . . . . . 
                                . . c 7 7 7 7 7 7 7 7 c . . . . 
                                . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                                . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                                . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                                . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                                . . f 7 7 7 7 6 c 7 7 6 f c . . 
                                . . . f c c c c 7 7 6 f 7 7 c . 
                                . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                                . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                                c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                                f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                                f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                                . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                                . . c c c c c c c c c f . . . .
                """),
                img("""
                    . . . c c c c c c . . . . . . . 
                                . . c 6 7 7 7 7 6 c . . . . . . 
                                . c 7 7 7 7 7 7 7 7 c . . . . . 
                                c 6 7 7 7 7 7 7 7 7 6 c . . . . 
                                c 7 c 6 6 6 6 c 7 7 7 c . . . . 
                                f 7 6 f 6 6 f 6 7 7 7 f . . . . 
                                f 7 7 7 7 7 7 7 7 7 7 f . . . . 
                                . f 7 7 7 7 6 c 7 7 6 f . . . . 
                                . . f c c c c 7 7 6 f c c c . . 
                                . . c 6 2 7 7 7 f c c 7 7 7 c . 
                                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c 
                                . c 1 1 1 1 7 6 6 c 6 6 6 c c c 
                                . c 1 1 1 1 1 6 6 6 6 6 6 c . . 
                                . c 6 1 1 1 1 1 6 6 6 6 6 c . . 
                                . . c 6 1 1 1 1 1 7 6 6 c c . . 
                                . . . c c c c c c c c c c . . .
                """)],
            100,
            False)
game.on_update_interval(5000, on_update_interval6)

def on_update_interval7():
    global Snake, statusbar
    if Current_level == 6:
        Snake = sprites.create(img("""
                . . . . c c c c c c . . . . . . 
                            . . . c 6 7 7 7 7 6 c . . . . . 
                            . . c 7 7 7 7 7 7 7 7 c . . . . 
                            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                            . . f 7 7 7 7 6 c 7 7 6 f c . . 
                            . . . f c c c c 7 7 6 f 7 7 c . 
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.enemy)
        Snake.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Snake)
        animation.run_image_animation(Snake,
            [img("""
                    . . . . c c c c c c . . . . . . 
                                . . . c 6 7 7 7 7 6 c . . . . . 
                                . . c 7 7 7 7 7 7 7 7 c . . . . 
                                . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                                . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                                . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                                . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                                . . f 7 7 7 7 6 c 7 7 6 f c . . 
                                . . . f c c c c 7 7 6 f 7 7 c . 
                                . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                                . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                                c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                                f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                                f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                                . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                                . . c c c c c c c c c f . . . .
                """),
                img("""
                    . . . c c c c c c . . . . . . . 
                                . . c 6 7 7 7 7 6 c . . . . . . 
                                . c 7 7 7 7 7 7 7 7 c . . . . . 
                                c 6 7 7 7 7 7 7 7 7 6 c . . . . 
                                c 7 c 6 6 6 6 c 7 7 7 c . . . . 
                                f 7 6 f 6 6 f 6 7 7 7 f . . . . 
                                f 7 7 7 7 7 7 7 7 7 7 f . . . . 
                                . f 7 7 7 7 6 c 7 7 6 f . . . . 
                                . . f c c c c 7 7 6 f c c c . . 
                                . . c 6 2 7 7 7 f c c 7 7 7 c . 
                                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c 
                                . c 1 1 1 1 7 6 6 c 6 6 6 c c c 
                                . c 1 1 1 1 1 6 6 6 6 6 6 c . . 
                                . c 6 1 1 1 1 1 6 6 6 6 6 c . . 
                                . . c 6 1 1 1 1 1 7 6 6 c c . . 
                                . . . c c c c c c c c c c . . .
                """)],
            100,
            False)
game.on_update_interval(5000, on_update_interval7)

def on_update_interval8():
    global Snake, statusbar
    if Current_level == 11:
        Snake = sprites.create(img("""
                . . . . c c c c c c . . . . . . 
                            . . . c 6 7 7 7 7 6 c . . . . . 
                            . . c 7 7 7 7 7 7 7 7 c . . . . 
                            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                            . . f 7 7 7 7 6 c 7 7 6 f c . . 
                            . . . f c c c c 7 7 6 f 7 7 c . 
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.enemy)
        Snake.set_position(randint(1, 255), randint(1, 255))
        statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(Snake)
        animation.run_image_animation(Snake,
            [img("""
                    . . . . c c c c c c . . . . . . 
                                . . . c 6 7 7 7 7 6 c . . . . . 
                                . . c 7 7 7 7 7 7 7 7 c . . . . 
                                . c 6 7 7 7 7 7 7 7 7 6 c . . . 
                                . c 7 c 6 6 6 6 c 7 7 7 c . . . 
                                . f 7 6 f 6 6 f 6 7 7 7 f . . . 
                                . f 7 7 7 7 7 7 7 7 7 7 f . . . 
                                . . f 7 7 7 7 6 c 7 7 6 f c . . 
                                . . . f c c c c 7 7 6 f 7 7 c . 
                                . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
                                . c 7 7 2 7 7 c f c 6 7 7 6 c c 
                                c 1 1 1 1 7 6 f c c 6 6 6 c . . 
                                f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
                                f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
                                . f 6 1 1 1 1 1 1 6 6 6 f . . . 
                                . . c c c c c c c c c f . . . .
                """),
                img("""
                    . . . c c c c c c . . . . . . . 
                                . . c 6 7 7 7 7 6 c . . . . . . 
                                . c 7 7 7 7 7 7 7 7 c . . . . . 
                                c 6 7 7 7 7 7 7 7 7 6 c . . . . 
                                c 7 c 6 6 6 6 c 7 7 7 c . . . . 
                                f 7 6 f 6 6 f 6 7 7 7 f . . . . 
                                f 7 7 7 7 7 7 7 7 7 7 f . . . . 
                                . f 7 7 7 7 6 c 7 7 6 f . . . . 
                                . . f c c c c 7 7 6 f c c c . . 
                                . . c 6 2 7 7 7 f c c 7 7 7 c . 
                                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c 
                                . c 1 1 1 1 7 6 6 c 6 6 6 c c c 
                                . c 1 1 1 1 1 6 6 6 6 6 6 c . . 
                                . c 6 1 1 1 1 1 6 6 6 6 6 c . . 
                                . . c 6 1 1 1 1 1 7 6 6 c c . . 
                                . . . c c c c c c c c c c . . .
                """)],
            100,
            False)
game.on_update_interval(5000, on_update_interval8)

def on_forever():
    music.play(music.create_song(hex("""
            0078000408020105001c000f0a006400f4010a00000400000000000000000000000000000000023f000000040002202a08000c0002222910001400012518001c00021d2c20002400031d242a28002c00031d242a30003400012438003c0001243c004000031e272a
        """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
