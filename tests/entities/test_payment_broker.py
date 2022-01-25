from banking_app.entities.payment_broker import PaymentBroker


def test_payment_broker_earnings_zero_after_init():
    payment_broker = PaymentBroker("something")
    assert payment_broker.earnings == 0, "Payment Broker always has 0 start earnings"
