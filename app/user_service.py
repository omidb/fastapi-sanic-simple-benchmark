from .share import User, Address
import random

class UserService:
    @staticmethod
    def create_address(user: User):
        # Log the incoming request
        # logger.info(f"Received user data: {json.dumps(user.model_dump(), default=str)}")
        
        # Generate random zip code
        zip = random.randint(10000, 99999)
        
        # Create and return address
        address = Address(
            street="742 Evergreen Terrace",
            city="Springfield",
            state="Oregon",
            zip=str(zip)
        )
        
        # logger.info(f"Returning address: {json.dumps(address.model_dump())}")
        return address