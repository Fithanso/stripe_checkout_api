import stripe

from stripe_payment import settings


class StripeManager:

    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_API_KEY

    def create_checkout_session(self, order_items):

        session = stripe.checkout.Session.create(
            line_items=self.create_line_items(order_items),
            mode='payment',
            success_url='http://example.com/success',
            cancel_url='http://example.com/cancel',
        )

        return session

    def create_line_items(self, order_items):
        line_items = []
        for order_item in order_items:

            line_items.append({
                'price_data': {
                    'currency': settings.STRIPE_CURRENCY,
                    'product_data': {
                        'name': order_item.item.name,
                    },
                    'unit_amount': order_item.item.price,
                },
                'quantity': order_item.quantity,
            })

        return line_items



