import stripe

from stripe_payment import settings


class StripeManager:

    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_API_KEY

    def create_checkout_session(self, item_name, item_price):
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': settings.STRIPE_CURRENCY,
                    'product_data': {
                        'name': item_name,
                    },
                    'unit_amount': item_price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://example.com/success',
            cancel_url='http://example.com/cancel',
        )

        return session
