import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_total_functions_appear_on_list_page(user_transactions, client):
    user = user_transactions[0].user
    client.force_login(user)

    income_total = sum(t.amount for t in user_transactions if t.type == 'income')
    expenses_total = sum(t.amount for t in user_transactions if t.type == 'expense')
    net = income_total - expenses_total

    response = client.get(reverse('transactions-list'))
    assert response.context['total_income'] == income_total
    assert response.context['total_expenses'] == expenses_total
    assert response.context['net_income'] == net
