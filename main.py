def on_a_pressed():
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    ball.set_velocity(70, 0)
    controller.move_sprite(ball, 0, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    effects.confetti.start_screen_effect(1000)
    resetPlayers()
    info.change_score_by(1)
    music.play(music.melody_playable(music.jump_up),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_countdown_end():
    if info.score() >= 4:
        game.set_game_over_effect(True, effects.confetti)
        game.game_over(True)
    else:
        game.set_game_over_effect(False, effects.slash)
        game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.melody_playable(music.wawawawaa),
        music.PlaybackMode.IN_BACKGROUND)
    resetPlayers()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def resetPlayers():
    ball.set_velocity(0, 0)
    ball.set_position(20, 60)
    controller.move_sprite(ball, 0, 50)
    goalie.set_position(130, 60)
    goalie.follow(ball, 20)
    animation.run_image_animation(goalie, assets.animation("""
        myAnim
        """), 200, True)
goalie: Sprite = None
ball: Sprite = None
info.set_score(0)
info.start_countdown(30)
scene.set_background_image(assets.image("""
    field
    """))
ball = sprites.create(assets.image("""
    ball
    """), SpriteKind.projectile)
goalie = sprites.create(assets.image("""
    goalie
    """), SpriteKind.enemy)
resetPlayers()
goal = sprites.create(assets.image("""
    goal
    """), SpriteKind.player)
goal.x = 160
characterAnimations.loop_frames(ball,
    assets.animation("""
        myAnim0
        """),
    100,
    characterAnimations.rule(Predicate.MOVING))