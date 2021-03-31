from consoleEngine import ConsoleEngine
import math


class FourierSeries:
    def __init__(self, sequence, fps=60, screenSize=(400, 400)):
        self.sequence = [[l, rs / fps * 360, 0] for l, rs in sequence]
        self.fps = fps
        self.screenSize = screenSize
        self.width, self.height = self.screenSize
        self.screen = ConsoleEngine(self.screenSize)
        self.midPoint = self.width / 2, self.height / 2

        self.run()

    def run(self):
        lastPoint = self.midPoint
        lastPoint = self.drawSeries(lastPoint)
        for _ in range(1000):
            lastPoint = self.drawSeries(lastPoint)

    def drawSeries(self, lastPoint):
        lastJoint = self.midPoint
        for index, line in enumerate(self.sequence):
            lineLength, rotation, angle = line

            angle = angle + rotation

            lastJoint = self.rotateLine(lastJoint, lineLength, angle)

            self.sequence[index][2] = angle

        self.screen.drawLine(lastPoint, lastJoint)
        # self.screen.drawPixel(lastJoint)
        return lastJoint

    def rotateLine(self, lastPoint, l, angle):
        x, y = lastPoint
        return self.rotatePoint(lastPoint, (x + l, y + l), angle, l)

    def rotatePoint(self, p1, p2, a, l, r=False, y=False):
        if a == 0: return p2

        a = a % 359
        x1, y1 = p1
        x2, y2 = p2

        d12 = l

        aP1P2 = math.atan2(y2 - y1, x2 - x1)  # In radians, not degrees
        aP1P3 = aP1P2 - math.radians(a)

        x3 = x1 + d12 * math.cos(aP1P3)
        y3 = y1 + d12 * math.sin(aP1P3)

        if r:
            x3 = round(x3, r)
            y3 = round(y3, r)

        return x3, y3


if __name__ == "__main__":
    sequence = [[10, 1.5], [50, 0], [20, 1.8], [-30, 0.2], [50, -2]]

    f = FourierSeries(sequence)
    f.screen.display()
    input()
