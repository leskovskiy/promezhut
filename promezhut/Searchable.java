package promezhut;

import java.util.List;

public interface Searchable{
    List<Toys> findToysByName (String name);
}
