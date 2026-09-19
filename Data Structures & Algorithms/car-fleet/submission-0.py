class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = sorted(zip(position,speed), reverse = True)
       
        fleets = 0
        maxtime = 0.0

        for p , s in cars:
            time = (target - p )/ s

            if time > maxtime:
                fleets += 1
                maxtime = time
       
        return fleets

