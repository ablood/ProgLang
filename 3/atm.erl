-module(atm).
-export([widthdraw/2]).

widthdraw(Amount, CurrentRest, [RestMax | RestTail])->
    if
        Amount > RestMax ->
            widthdraw(Amount - RestMax, [RestMax|CurrentRest], RestTail);
        Amount < RestMax ->
            widthdraw(Amount, CurrentRest, RestTail);
        true ->
            {ok, CurrentRest ++ [RestMax]}
    end;
widthdraw(_, _, []) ->
    {request_another_amount, []}.

widthdraw(Amount, Banknotes)->
    Sorted = lists:sort(fun(A, B) -> A >= B end, Banknotes),
    case widthdraw(Amount, [], Sorted) of
        {ok, Rest} ->
            {ok, Rest, Banknotes -- Rest};
        {request_another_amount, []} ->
            {request_another_amount, [], Banknotes}
    end.