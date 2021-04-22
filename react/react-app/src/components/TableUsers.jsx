import React, { Component } from 'react'
import Table from 'react-bootstrap/Table'

class TableUsers extends Component {



    render() {
        // const { users, updateUser } = this.props;
        return (
            <div className="col-md-5">
                <Table responsive="md" striped bordered hover size="sm">
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Username</th>
                        <th>Avatar</th>
                        <th>Phone Number</th>
                        <th>Created At</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {this.props.users.map(user => (
                        <tr>
                            <td>{user.id}</td>
                            <td>{user.name}</td>
                            <td>{user.email}</td>
                            <td>{user.username}</td>
                            <td>{user.avatar}</td>
                            <td>{user.phoneNumber}</td>
                            <td>{user.createdAt}</td>
                            <td>
                                <button
                                    onClick={() => this.props.updateUser(user.id, `${user.name}a`)}
                                    className="bt btn-success"
                                >
                                    Edit
                                </button></td>
                        </tr>
                    ))}
                   
                </tbody>
            </Table>
            </div>
         );
    }
}
 
export default TableUsers;