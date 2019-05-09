from platforms import Platform


class Wall(Platform):
    """
    Klasa ściany (pionowa platforma)
    """

    def draw(self, surface, image_list_wall, image_list_wall_corner):
        for row in range(0, self.height, 70):
            if row == 0:
                surface.blit(image_list_wall_corner[0], self.rect)
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[2], [self.rect.x + column, self.rect.y])
                surface.blit(image_list_wall_corner[1],
                             [self.rect.x + self.width - 70, self.rect.y])

            elif row == self.height - 70:
                surface.blit(image_list_wall_corner[3],
                             [self.rect.x, self.rect.y + row])
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[4],
                        [self.rect.x + column, self.rect.y + row])
                surface.blit(image_list_wall_corner[2],
                             [self.rect.x + self.width - 70, self.rect.y + row])

            else:
                surface.blit(image_list_wall[1],
                             [self.rect.x, self.rect.y + row])
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[0],
                        [self.rect.x + column, self.rect.y + row])
                surface.blit(image_list_wall[3],
                             [self.rect.x + self.width - 70, self.rect.y + row])
