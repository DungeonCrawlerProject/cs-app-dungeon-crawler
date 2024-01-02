import math
from dataclasses import dataclass

import pygame

from Scripts.Player.Movement.player_stats import PlayerStats
from Scripts.Player.PlayerStateMachine.PlayerStates.player_idle import PlayerIdle
from Scripts.Player.PlayerStateMachine.PlayerStates.player_move import PlayerMove
from Scripts.Player.PlayerStateMachine.PlayerStates.player_dodge import PlayerDodge
from Scripts.Player.PlayerStateMachine.player_state import IPlayerState

# TODO Position is temp
@dataclass
class Position:
    x: float
    y: float

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, start_position, group):
        super().__init__(group)
        self.image = pygame.image.load('Sprites/Player.png').convert_alpha()
        self.rect = self.image.get_rect(center = start_position)
 

class Player:
    position: Position
    stats: PlayerStats = PlayerStats()
    angle: float = 0

    def __init__(self, start_position, camera):
        self.player_sprite = PlayerSprite(start_position, camera)
        camera.add(self.player_sprite)

       # Note: the real state should be Idle once statemachine is added properly
        self.current_state: IPlayerState = PlayerMove
        self.mouse_position = (0, 0)

    def update(self) -> None:

        # currentState = currentState.DoState(this);
        self.mouse_position = pygame.mouse.get_pos()

        # TODO make it actually call for the player state, these should also be fixed update
        if self.current_state == PlayerMove:
            PlayerMove.move(self)

        if self.current_state == PlayerIdle:
            raise NotImplementedError

        if self.current_state == PlayerDodge:
            raise NotImplementedError

        # TODO un_hardcode, Should be fixed update
        player_size = 50

        # currentState = currentState.DoState(this);
        self.mouse_position = pygame.mouse.get_pos()

        # Get the mouse position
        mouse_x, mouse_y = self.mouse_position

        self.angle = math.degrees(
            math.atan2(
                mouse_y - (self.position.y + player_size // 2),
                mouse_x - (self.position.x + player_size // 2)
            )
        )

    def take_damage(self, damage: float):

        self.stats.current_health -= damage

        # healthBar.SetHealth(curHealth / maxHealth);

        if self.stats.current_health < 0:
            self.kill_player()

    def kill_player(self):
        raise NotImplementedError
