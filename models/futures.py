from db import db
from datetime import datetime


class CoinbaseFuture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=True)
    price_change_24h = db.Column(db.Float, nullable=True)
    volume_24h = db.Column(db.Float, nullable=True)
    volume_change_24h = db.Column(db.Float, nullable=True)
    # quote_increment = db.Column(db.Float, nullable=True)
    # quote_min_size = db.Column(db.Float, nullable=True)
    # quote_max_size = db.Column(db.Float, nullable=True)
    # base_min_size = db.Column(db.Float, nullable=True)
    # base_max_size = db.Column(db.Float, nullable=True)
    # base_name = db.Column(db.String(128), nullable=True)
    # quote_name = db.Column(db.String(128), nullable=True)
    display_name = db.Column(db.String(128), nullable=True)
    product_type = db.Column(db.String(64), nullable=True)
    contract_expiry = db.Column(db.DateTime, nullable=True)
    contract_size = db.Column(db.Float, nullable=True)
    contract_root_unit = db.Column(db.String(64), nullable=True)
    # venue = db.Column(db.String(64), nullable=True)
    status = db.Column(db.String(64), nullable=True)
    trading_disabled = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f'<CoinbaseFuture {self.display_name} {self.product_id}>'


class AccountBalanceSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.String(64), nullable=True)
    available_margin = db.Column(db.Float, nullable=True)
    cbi_usd_balance = db.Column(db.Float, nullable=True)
    cfm_usd_balance = db.Column(db.Float, nullable=True)
    daily_realized_pnl = db.Column(db.Float, nullable=True)
    futures_buying_power = db.Column(db.Float, nullable=True)
    initial_margin = db.Column(db.Float, nullable=True)
    liquidation_buffer_amount = db.Column(db.Float, nullable=True)
    liquidation_buffer_percentage = db.Column(db.Integer, nullable=True)
    liquidation_threshold = db.Column(db.Float, nullable=True)
    total_open_orders_hold_amount = db.Column(db.Float, nullable=True)
    total_usd_balance = db.Column(db.Float, nullable=True)
    unrealized_pnl = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<AccountBalanceSummary {self.id} - Total CFM USD Balance: {self.cfm_usd_balance}>'


class FuturesOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(128), nullable=True)
    product_id = db.Column(db.String(128), nullable=True)
    side = db.Column(db.String(32), nullable=True)
    client_order_id = db.Column(db.String(128), nullable=True)
    success = db.Column(db.Boolean, nullable=False, default=False)
    failure_reason = db.Column(db.String(255), nullable=True)
    error_message = db.Column(db.String(255), nullable=True)
    error_details = db.Column(db.String(255), nullable=True)
    order_type = db.Column(db.String(128), nullable=True)
    quote_size = db.Column(db.String(128), nullable=True)
    base_size = db.Column(db.String(128), nullable=True)
    limit_price = db.Column(db.String(128), nullable=True)
    leverage = db.Column(db.String(128), nullable=True)
    # stop_price = db.Column(db.String(128), nullable=True)
    post_only = db.Column(db.Boolean, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<FuturesOrder {self.order_id} - {self.product_id} - {self.side}>'


class FuturePosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(128), nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)
    side = db.Column(db.String(10), nullable=False)
    number_of_contracts = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Float, nullable=True)
    avg_entry_price = db.Column(db.Float, nullable=True)
    unrealized_pnl = db.Column(db.Float, nullable=True)
    daily_realized_pnl = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<FuturePosition {self.product_id} {self.side}>'
