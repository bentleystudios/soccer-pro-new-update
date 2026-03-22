controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    ball.setVelocity(70, 0)
    controller.moveSprite(ball, 0, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite, otherSprite) {
    effects.confetti.startScreenEffect(500)
    resetPlayers()
    info.changeScoreBy(2)
    music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.InBackground)
})
info.onCountdownEnd(function () {
    if (info.score() >= 8) {
        game.setGameOverEffect(true, effects.confetti)
        game.gameOver(true)
    } else {
        game.setGameOverEffect(false, effects.slash)
        game.gameOver(false)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.wawawawaa), music.PlaybackMode.InBackground)
    resetPlayers()
})
function resetPlayers () {
    ball.setVelocity(0, 0)
    ball.setPosition(20, 60)
    controller.moveSprite(ball, 0, 50)
    goalie.setPosition(130, 60)
    goalie.follow(ball, 20)
    animation.runImageAnimation(
    goalie,
    assets.animation`myAnim`,
    200,
    true
    )
}
let goalie: Sprite = null
let ball: Sprite = null
info.setScore(0)
info.startCountdown(30)
scene.setBackgroundImage(assets.image`field`)
ball = sprites.create(assets.image`ball`, SpriteKind.Projectile)
goalie = sprites.create(assets.image`goalie`, SpriteKind.Enemy)
resetPlayers()
let goal = sprites.create(assets.image`goal`, SpriteKind.Player)
goal.x = 160
characterAnimations.loopFrames(
ball,
assets.animation`myAnim0`,
100,
characterAnimations.rule(Predicate.Moving)
)
